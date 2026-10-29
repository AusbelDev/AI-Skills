# JobRunner Jobs That Drive an Interface

Use this when an interface needs a job: a manual or bulk export (cutover, reconciliation,
"send everything for block month X"), a scheduled export, or a job that feeds an IOService
which a trigger also feeds. The core API is `jobrunner.version_1.api` under `$CARMSYS`; the
site's jobs live in a `Jobs(api.JobDefinitionsBase)` class in the `usr` layer (look for a
`jobrunner_ext/job_definitions.py` or grep `JobDefinitionsBase` under `$CARMUSR/lib/python`).

## Anatomy of a job definition

Jobs are entries in the `jobs` dict of the `Jobs` class:

```python
"export_roster_out_odh_fops": {
    "name": "Export FOPS Roster Out to ODH",      # shown in the Jobrunner UI
    "desc": "...",
    "queue": "to.ioservice.JobrunnerExecuter",     # decides who runs it, see below
    "pattern": None,                               # cron string for scheduled, None = manual only
    "parameters": {
        "bid_month": {
            "required": True,
            "valueType": api.ValueTypes.SELECT,    # SELECT, STRING, INT, FLOAT, BOOL, DATE, TIME, DATETIME, TIMEDELTA
            "desc": "...",
            "index": 1,                            # order in the UI
            "regex": r"^[\w.-]+$",
        },
        ...
    },
},
```

A definition alone is not enough. The `Jobs` class answers the UI through methods that are
usually long `if job_id in (...)` chains, and a new job has to be added to each chain it needs:

| Method | What it provides | Symptom if the job is missing from it |
| :--- | :--- | :--- |
| `get_param_values(job_id, param_name)` | The options of a SELECT parameter | Empty dropdown |
| `get_default_value(job_id, param_name, start_time)` | Pre-filled parameter values | No default, or the wrong one |
| `get_message_body(job_instance)` | The request body for `to.job.*` jobs | Route gets an empty body |
| `execute_job(job_context)` | The Python that runs `JobrunnerExecuter` jobs | **Silent no-op, see below** |

Grep for a sibling job's id (a job with the same parameters) to find every chain to extend.

## Two ways a job runs

The `queue` of the definition decides where the work happens:

- **`to.job.<name>`** — a Camel route (usually in `clusterroutes.xml`) consumes the job
  message, forwards the body from `get_message_body` to an IOService, and reports back to
  Jobrunner. Fine for "one request, one file". Needs a route; without one the job sits in
  the queue forever.
- **`to.ioservice.JobrunnerExecuter`** — the job runs as Python in `execute_job(job_context)`
  inside an IOServer (`jobrunner_exec.xml`, typically `worker_time_out` 600 s). Use it when
  the job needs logic: loops, per-entity messages, filtering in the plan, several requests.
  No route needed.

## Rules for executer jobs

1. **Dispatch it in `execute_job`.** The base `execute_job` returns `None`, and the framework
   then falls back to a default result with `save_plan=True`. A job missing from the dispatch
   chain therefore "succeeds", does nothing, and saves the plan. Add the dispatch together
   with the method it calls; never deploy a definition on the executer queue without it.
2. **Return `job_context.result(save_plan=False)`** from jobs that only read the plan, which
   is every export.
3. **Parameters arrive in `job_context.job_message_headers`**, as strings. Optional
   parameters can be absent or empty, so treat falsy as "not set".
4. **Validate before sending anything.** `job_context.fail(reason)` raises
   `JobFailedException` and shows the reason on the job instance. Check unknown ids, missing
   periods, and out-of-range periods up front, so a bad input can't produce a partial export.
5. **Ping in long loops.** `request_ioservice` blocks without pinging the worker, and a loop
   over thousands of entities can run past `worker_time_out`. Call
   `job_context.service_context.report_progress()` every N items, and `set_remark(...)` so
   the UI shows progress.

## `send_message` vs `request_ioservice` — pick by where the response must go

This is the decision that most often goes wrong:

| Call | What it does | Use when |
| :--- | :--- | :--- |
| `job_context.request_ioservice(queue, content, headers, timeout)` | Sets **reply-to** and waits; the IOService sends its response (or fault) back to the job | The job itself handles the response, e.g. attaches it with `set_output_file` or writes a file |
| `job_context.send_message(queue, content, headers)` | Fire-and-forget; the IOService sends its response to its own configured `<sink>` | The response must take the service's existing path, e.g. the Camel route that already delivers the trigger's messages |

Because `request_ioservice` sets reply-to, the response **never reaches the service's sink
or its route**. A job that should feed an existing outbound route must use `send_message`.
The flip side: with reply-to, faults also come back to the job instead of the
`from.ioservice.<name>.error` sink, so a `request_ioservice` job has to publish the fault to
the error queue itself (before calling `fail`, which raises).

**Mutable-default trap:** `send_message` is declared `headers={}` and adds the job headers to
the dict it receives. Pass a new dict on every call (`headers={}` in the call creates one);
never reuse one dict across a loop.

## Feeding a service that a trigger also feeds

A common cutover need: "send everything once, the way the trigger sends changes."

- **Reuse the trigger's request builder** (look in the trigger's `handler.py`, e.g. a
  `MessageGenerator`), so job and trigger messages are identical and the service, route and
  receiver need no changes.
- **Keep the trigger's granularity.** If the receiver partitions on an id (e.g. Kafka keyed
  on crew id), send one entity per message; a grouped bulk message breaks the partitioning.
- **Clip the period to the loaded data period.** std_interfaces services reject requests
  outside it (`validate_times_with_plan_period`). Read it from the plan's parameter set
  (`plan.getDataContext().getParameterSet()`, parameters `data_period_start` /
  `data_period_end`; the executer job gets the plan via
  `job_context.planholder.getMave2Plan()`), clip, and fail if nothing is left. Many sites
  already have helpers for this next to their triggers; reuse them.
- **Two producers on one queue changes ordering.** The trigger and the job now both feed the
  service, so where and how many times the service runs matters. See "Placing a service on
  IOServer processes" in `SKILL.md`, and raise the ordering question with the user before
  deploying.
- **Expect delay.** A bulk job queues thousands of requests in front of the trigger's, and the
  service works through them with its worker pool. Say so in the docs.
