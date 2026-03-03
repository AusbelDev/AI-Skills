## Module overview

### Rave Python API


This module provides a Python interface to Rave evaluations and definitions. It cannot be used on its own, it must be run from within a Rave-enabled application.
For the Atrium architecture, a Rave ruleset may be loaded by creating a [`Ruleset`](stubs/carmensystems.rave.api.Ruleset.html#carmensystems.rave.api.Ruleset "carmensystems.rave.api.Ruleset") instance, but for an application in the old architecture, the ruleset is always loaded by the application itself. In the latter case, a Ruleset instance can be retrieved from the function `getApplicationLoaded()`.

The basic concepts of the API are explained below. Readers are assumed to be familiar with the Rave language.

Throughout this documentation, *italics* is used to show the definition of a term can be found via the index (under **Indices** at the top of the page).

##### Rave values

A Rave value is an object that can be returned by Rave, or passed as argument to a Rave function. Its type must correspond to one of Rave’s data types. Instances of the following types are valid Rave values:
:   * `int`
    * `bool`
    * `string`
    * `AbsTime`
    * `RelTime`
    * [`enumval`](api.html#carmensystems.rave.api.enumval "carmensystems.rave.api.enumval") (`enum` value)

`AbsTime` and `RelTime` are defined in the `carmensystems.basics` package, but are also made available by this API.

`None` is also a valid Rave value, corresponding to `void` in Rave. Note however that Rave functions do not accept `void` values as function arguments.

##### Rave definitions

The [`Definition`](stubs/carmensystems.rave.api.Definition.html#carmensystems.rave.api.Definition "carmensystems.rave.api.Definition") class hierarchy represent things definied in Rave, either by the user (variables, levels, iterators etc.) or by the application’s configuration (keywords, contexts, transforms).

You rarely need to create Definition objects; functions and methods that require Definition arguments also accept definition names (strings).

Note that `global export` does not apply outside the Rave code; definition names must include the module name, unless they are built-in or defined in the `_topmodule`.

##### Evaluators

An evaluator is an object capable of computing *Rave values* . Instances of the following types are evaluators:
:   * [`Computable`](stubs/carmensystems.rave.api.Computable.html#carmensystems.rave.api.Computable "carmensystems.rave.api.Computable") (Rave definitions: variables, keywords, rules etc.)
    * [`expr`](api.html#carmensystems.rave.api.expr "carmensystems.rave.api.expr") (Rave expressions)
    * [`Traverser`](stubs/carmensystems.rave.api.Traverser.html#carmensystems.rave.api.Traverser "carmensystems.rave.api.Traverser") (evaluation on a sub-level)
    * [`foreach`](api.html#carmensystems.rave.api.foreach "carmensystems.rave.api.foreach") (batch-evaluation using an iterator)

In addition, types listed under **Rave values** above are considered trivial evaluators; they evaluate to themselves.

Functions and methods that require *evaluator* arguments will also accept strings that are either names of [`Computable`](stubs/carmensystems.rave.api.Computable.html#carmensystems.rave.api.Computable "carmensystems.rave.api.Computable")s, or valid arguments to the [`expr`](api.html#carmensystems.rave.api.expr "carmensystems.rave.api.expr") constructor.

###### Scalar evaluators

A scalar evaluator is an evaluator that computes a single Rave value. Valid scalar evaluators are instances of all types listed above except [`foreach`](api.html#carmensystems.rave.api.foreach "carmensystems.rave.api.foreach").

###### Dependency level

All evaluators have a dependency level: the Rave level required to be able to compute the value. The level used in the evaluation must be less or equal to the dependency level.

The built-in `const` level is in this sense considered greater than any other level, so evaluators with `const` dependency can be computed on any level.

##### Using Rave iterators

The application’s planning data can be traversed using Rave iterators. There are two ways to do this in the API: call [`eval()`](stubs/carmensystems.rave.api.eval.html#carmensystems.rave.api.eval "carmensystems.rave.api.eval") with a [`foreach`](api.html#carmensystems.rave.api.foreach "carmensystems.rave.api.foreach") argument, or use the **Bag interface** described below.

When using a `foreach`, all data is computed in one call, and the results are returned in a list/tuple structure . An [`Iteration`](stubs/carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") object specifies the iteration.

When using the Bag interface, contexts are traversed using ordinary python iterators, and values are computed as you go along.

##### The Bag interface

The Bag interface offers a convenient way of using Rave iterators and evaluating Rave definitions. Objects implementing the interface have a dynamic set of attributes, generated by Rave definitions in the loaded ruleset.

A **Bag** is an object representing a number of planning objects. It could be anything from all chains in a context to just a single leg. There is no single Bag class in the API; the interface is implemented by a number of specialised private classes. The user gains access to bag instances by calling e.g. the [`Context.bag()`](stubs/carmensystems.rave.api.Context.html#carmensystems.rave.api.Context.bag "carmensystems.rave.api.Context.bag") method, which returns the context’s content as a bag, or by using Bag interface iterators, all of which return bags.

A bag object supports the following operations:
:   * evaluation of [`Computable`](stubs/carmensystems.rave.api.Computable.html#carmensystems.rave.api.Computable "carmensystems.rave.api.Computable")s
    * traversal using Rave iterators
    * applying transforms

It can also be passed as first argument to [`eval()`](stubs/carmensystems.rave.api.eval.html#carmensystems.rave.api.eval "carmensystems.rave.api.eval").

###### Evaluating Computables

Any computable is a callable attribute on a bag, so if `leg` is a bag containing a single leg object, the expression:

```
leg.arrival()
```

will return the *Rave value* of the keyword `arrival`, evaluated on that leg.

Rules, constraints and variables can be evaluated in the same way. But in general, these are defined in a module. To evaluate e.g. `task.%code%` on the bag above, the syntax is:

```
leg.task.code()
```

The module – `leg.task` in the example – is represented by a special bag object. It contains the same objects as the bag it originated from – `leg` in the example – but it is bound to a particular Rave module, and only implements a subset of the Bag interface: Definitions made in that module are attributes, other definitions are not available.

Since ‘%’ characters are not allowed in Python identifiers, they must be stripped from variable names used as bag attributes. This could cause name clashes between variables defined in the `_topmodule` and other definitions; one definition will ‘hide’ the other. See section *Name clashes?* under **\*Troubleshooting\*** below.

For keywords and variables that are functions, the call will take arguments, e.g.:

```
leg.booked_crew_position(1)
```

The arguments must be valid *Rave value* s; void (`None`) is not accepted.

The *dependency level* of the computable must match the content of the bag, or an exception will be raised. It is e.g not possible to evaluate an atom-level keyword on a bag containing a higher-level object or a whole context.

###### Using iterators

Iterators are applied in the same way, but the return value from the call is a Python iterator, not a *Rave value* . The iterator returns new bag objects that can be used for evaluating computables or applying new iterators. Example:

```
all_crew = ... # a Context object
#### apply built-in iterator 'chain_set' to the context bag
for roster in all_crew.bag().chain_set():
    # evaluate variable 'crew.%id%' on the roster
    id = roster.crew.id()
    # apply iterator 'iterators.trip_set' to the roster
    for trip in roster.iterators.trip_set():
        ... # evaluate trip values
```

Like the functions that create [`Iteration`](stubs/carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration")s, the iterator call takes two optional arguments, `where` and `sort_by`, that enable filtering and sorting. See [`iter()`](stubs/carmensystems.rave.api.iter.html#carmensystems.rave.api.iter "carmensystems.rave.api.iter") for a detailed description of these parameters.

Iterators that have no defined level, e.g. the predefined iterator `times`, cannot be used with the Bag interface.

The Bag interface also provides two built-in iterators, that return (bag, [`LoopData`](stubs/carmensystems.rave.api.LoopData.html#carmensystems.rave.api.LoopData "carmensystems.rave.api.LoopData")) tuples instead of just bags:
:   * **rulefailures(where=None, sort\_by=None, group=None)**

      > Corresponds exactly to the [`Iteration`](stubs/carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") created by [`rulefailure()`](stubs/carmensystems.rave.api.rulefailure.html#carmensystems.rave.api.rulefailure "carmensystems.rave.api.rulefailure"); see this entry for more details. Returns (bag, [`RuleFail`](stubs/carmensystems.rave.api.RuleFail.html#carmensystems.rave.api.RuleFail "carmensystems.rave.api.RuleFail")) tuples. The level of the bag is determined by the dependency of the rule.
    * **constraint\_evals(where=None, sort\_by=None)**

      > Corresponds exactly to the [`Iteration`](stubs/carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") created by [`constraint_eval()`](stubs/carmensystems.rave.api.constraint_eval.html#carmensystems.rave.api.constraint_eval "carmensystems.rave.api.constraint_eval"); see this entry for more details. Returns (bag, [`ConstraintEval`](stubs/carmensystems.rave.api.ConstraintEval.html#carmensystems.rave.api.ConstraintEval "carmensystems.rave.api.ConstraintEval")) tuples. The level of the bag is determined by the dependency of the constraint.

Examples:

```
for crew in all_crew.bag().chain_set():
    id = crew.crew.id()
    for bag, fail in crew.rulefailures():
        process_rulefail(id, bag, fail)
    for bag, eval in crew.constraint_evals():
        if eval.overshoot:
            process_constraint_fail(id, bag, eval)
```

Note that **constraint\_evals()** only evaluates chain-dependent (transform) constraints, since bags are always a subset of a set-up context. Module function [`global_constraint_evals()`](stubs/carmensystems.rave.api.global_constraint_evals.html#carmensystems.rave.api.global_constraint_evals "carmensystems.rave.api.global_constraint_evals") returns the same kind of iterator for global (context) constraints.

###### Using transforms

Applying a transform to a bag returns a new bag, containing the objects returned by the transform. This bag can be used for evaluations and traversal just like any other bag:

```
equal_legs = leg.equal_legs()
for otherleg in equal_legs.iterators.leg_set():
    ...
```

###### The active bag

The Bag interface can only be used on one object at the time, the active bag. This is always the bag last created. Calling a bag that is not active will raise an exception. This means it is not possible to save a bag in a variable for later use, or use a bag from a previous loop.

The following is e.g. not allowed:

```
for crew in all_crew.bag().chain_set():
    for bag, fail in crew.rulefailures():
        id = crew.crew.id() # ERROR: 'bag' is now the active bag,
        ...                 # 'crew' is no longer active
```

`crew.%id%` must be evaluated before entering the `rulefailures` loop.

This will not work either:

```
prev = None
for leg in somebag.iterators.leg_set():
    if prev:
        process(leg.arrival(),
                prev.arrival()) # ERROR: 'prev' is no longer active
    prev = leg
```

It has to be rewritten into something like:

```
prev_arrival = None
for leg in somebag.iterators.leg_set():
    this_arrival = leg.arrival()
    if prev_arrival:
        process(this_arrival,
                prev_arrival)
    prev_arrival = this_arrival
```

###### CAPI

The Bag interface also provides the following CAPI-specific method:

**capi\_test(from, to, step)**

This method calls an external Common Alertness
Prediction Interface (CAPI) module in test mode and returns a list of
prediction values for the given time window. The module
must conform to CAPI V1.0 or V2.0.

*Parameters* :
**from** : Start time.
**to** : End time (not inclusive).
**step** : Step length.

*Returns* :
A list of integers in the range [1..9999] (negated in case of rest), or zero (0) for no prediction.

*Raises* :
[`InternalError`](stubs/carmensystems.rave.api.InternalError.html#carmensystems.rave.api.InternalError "carmensystems.rave.api.InternalError") if the external CAPI module cannot be loaded.
[`UsageError`](stubs/carmensystems.rave.api.UsageError.html#carmensystems.rave.api.UsageError "carmensystems.rave.api.UsageError") if Rave CAPI definitions are wrong or if no legs are involved.
`ValueError` if the result list is too large (> 100000 items) or if invalid arguments are given.

#### Rave values

#### Rave definitions

#### Evaluators

##### Scalar evaluators

##### Dependency level

#### Using Rave iterators

#### The Bag interface

##### Evaluating Computables

##### Using iterators

##### Using transforms

##### The active bag

##### CAPI

### Troubleshooting


##### Ruleset loaded?

Most functions and classes will raise an exception if there is no ruleset loaded. Also, unloading the ruleset will invalidate all ruleset-dependent objects created before unloading. Use function [`ruleset_loaded()`](stubs/carmensystems.rave.api.ruleset_loaded.html#carmensystems.rave.api.ruleset_loaded "carmensystems.rave.api.ruleset_loaded") to check if there is a ruleset.

##### Name clashes?

Since ‘%’ characters are not required in variable names passed to [`eval()`](stubs/carmensystems.rave.api.eval.html#carmensystems.rave.api.eval "carmensystems.rave.api.eval"), and cannot be part of *Bag* attribute names, name clashes may occur if a variable has the same name as another definition. This is not likely to happen in rulesets using modules and good naming standards. But if it does – and the ruleset cannot be changed – apply the workarounds suggested below.

###### Using eval()

Variables may clash with keywords, rules or constraints with the same name. If e.g. the ruleset has a keyword `arrival` and a `_topmodule` variable `%arrival%`, passing the string `'arrival'` to eval() will evaluate the variable, not the keyword; the variable will ‘hide’ the keyword. This can be solved by explicitly passing a keyword object instead of just a name:

```
keyw('arrival').
```

###### Using the Bag interface

Using bag attributes, definitions can be hidden in the same way. Using the example above, the call `leg.arrival()` will evaluate the variable, not the keyword. The workaround is to use eval() instead of calling the bag:

```
eval(leg, keyw('arrival'))
```

Other clashes are possible. Modules and iterators may hide variables, and the ‘fixed’ methods `rulefailures` and `constraint_evals` may be hidden if modules or `_topmodule` definitions are given these names. In all cases, `eval()` can be used as a workaround.

|  |  |
| --- | --- |
| var PROFILER\_NOT\_AVAILABLE: | One of the possible profiler states returned by [`profiler_status()`](stubs/carmensystems.rave.api.profiler_status.html#carmensystems.rave.api.profiler_status "carmensystems.rave.api.profiler_status"). |
| type PROFILER\_NOT\_AVAILABLE: | `int` |
| var PROFILER\_AVAILABLE: | One of the possible profiler states returned by [`profiler_status()`](stubs/carmensystems.rave.api.profiler_status.html#carmensystems.rave.api.profiler_status "carmensystems.rave.api.profiler_status"). |
| type PROFILER\_AVAILABLE: | `int` |
| var PROFILER\_INITIALIZED: | One of the possible profiler states returned by [`profiler_status()`](stubs/carmensystems.rave.api.profiler_status.html#carmensystems.rave.api.profiler_status "carmensystems.rave.api.profiler_status"). |
| type PROFILER\_INITIALIZED: | `int` |
| var PROFILER\_RUNNING: | One of the possible profiler states returned by [`profiler_status()`](stubs/carmensystems.rave.api.profiler_status.html#carmensystems.rave.api.profiler_status "carmensystems.rave.api.profiler_status"). |
| type PROFILER\_RUNNING: | `int` |

#### Ruleset loaded?

#### Name clashes?

##### Using eval()

##### Using the Bag interface