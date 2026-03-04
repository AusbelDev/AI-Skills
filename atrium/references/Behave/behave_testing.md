# 4.1. Behave

This document contains some guidelines when working with the automated test suite using Behave. Behave is mostly used to test legality (Rave rules) and Python reports. There are some test cases that look at the configuration for common errors that usually show up only in logfiles. Behave steps are also used in datafeed tests to create data.

---

## 4.1.1. Terminology

Behave uses its own terminology when it comes to test cases.

### Step - 1 sentence
Typically one line, written in English. The step consists of a fixed text and some input. When running a test case input is shown as bold text. Some steps take a table input. Table input is in the next line after the fixed test and consists of at least two lines: a mandatory heading line and at least one line of input.

Steps are grouped into:
* **do steps (Given, When):** steps that create or modify data, call other processes like generating a report, calling the accumulator, roster publication, etc.
* **observe steps (Then):** steps that do not modify anything, they are observing the state to check if it is as it is expected.

The step types `And` and `But` copy the type of the previously executed step.

### Scenario - 1 test case
A scenario consists of at least one step. Inside a scenario the steps are executed from top to bottom and behave stops the execution of a scenario on the first failing step. A typical flow of the scenario is: given an initial situation, when something happens, then something is expected to be in a certain way. In Atrium behave scenarios the step types can be mixed during the execution: it is possible to execute a `Given` step after a `Then` step.

In behave each scenario is executed independent from each other (except when running in persist mode). Changes are rolled back between scenarios. In the beginning of each scenario the following is available:
* An opened plan (using a specific datacontext)
* Containing catalog data only
* A loaded rave ruleset and parameter set
* The now-time set (please note: not using the simulated time)

### Feature - 1 file
Often referred to as feature-file. A feature contains a group of scenarios around a feature (e.g., rest rules, open_time report, etc.). It is possible to group several features together by using subfolders (e.g., `reports/`, `EASA/`, `exchange/`).

### Test suite - several test scenarios grouped together
The purpose is to be able to run test suites with different Rave rulesets (e.g., joc, jta).

---

## 4.1.2. Usage (Cheat Sheet)

### Setup the environment
From `cmsshell` run:
```bash
behave setup
```
This will:
* Compile ruleset(s)
* Build interfaces
* (Re)create the test database
* Populate the test database with catalog data (codes, types, homebase, roles, mock interface data, etc., but no flights/trips/crew).

### Run all tests
```bash
behave test
```
**Output indicators:**
* `.` = passed test
* `S` = skipped (ignored) test
* `F` = failed test

### Rerun failed test(s) only
```bash
behave rerun
```

### Rerun a single test only
Copy-paste the line from the Failing scenarios output:
```bash
behave scenario "features/self_test.feature:3 1a pact st"
```

### Run a whole feature file / selected scenarios
```bash
behave run --i rest --n 3.1.5
```

### Save results and open in Tracking Editor
First save the results of a run:
```bash
behave rerun --persist=1
behave persist --i rest --n 3.1.5
behave scenario --persist=1 "features/self_test.feature:3 1a pact st"
```
Then start a Launcher inside the confbox, use a browser to connect to `http://localhost:8080/`, and start a Tracking Editor with the developer role.

### Find ignored scenarios
```bash
behave tags
```

### Find behave steps
A behave step catalog is available on the documentation page created by each usr build under "Behave step definitions". To generate locally:
```bash
pipeline run --name=Documentation
firefox $CARMTMP/rst_target/index.html
```

---

## 4.1.3. General Guidelines

### Simple test cases
Keep test cases simple and well-structured. Avoid testing unrelated things in the same scenario. Use only information relevant for the test case. Test complex Rave calculations directly if possible to avoid an explosion of test cases.

### Comments
Add comments if unclear. The first lines after defining a feature or scenario are freetext comments. Use `And remark: freetext-here` for comments between steps. Empty headings in tables can also be used for comments:
```gherkin
Given a trip with the following activities
  | st    | et    | ades |                         |
  | 10:00 | 11:00 | BOS  |                         |
  | 12:00 | 13:00 | JFK  | not ending at trip base |
```

### Formatting
Use `ctrl + shift + f` in the Developer’s WorkSpace (DWS) to automatically format a feature-file.

---

## 4.1.4. How to refer to objects on a chain

Resources (Crewmember, Trip, Aircraft, etc.) are referenced in the order of creation. Once connected, steps refer to Assignments or Rave level objects.

**Examples:**
* `Then the Rave variable "leg.%is_reserve%" should evaluate to "True" for leg #4 of crewmember #2`
* `Then the Rave variable "leg.%is_reserve%" should evaluate to "True" for leg #1 in trip #2 for crewmember #2`

**Rave variables for identification:**
* `leg.%num_in_chain%` - e.g., leg #4 of crewmember #2
* `trip.%trip_num_in_roster%` - e.g., trip #2 for crewmember #2
* `leg.%leg_num_in_trip%` - e.g., leg #1 in trip #2 for crewmember #2

**Special word:** `last` can refer to the last created resource or object in a chain.
```gherkin
Then the Rave variable "leg.%is_reserve%" should evaluate to "True" for leg #1 in trip #last for crewmember #last
```

---

## 4.1.5. Scenario Outline

Use `Scenario Outline` to avoid maintaining multiple similar scenarios for success/failure cases.

**Example (Edge Case):**
```gherkin
Scenario Outline: 004 min_connection time rule
  Given a trip with the following activities
    | st    | et    |
    | 09:00 | 12:00 |
    | <end> | 17:00 |
   Then the Rave variable "leg.%connection_time%" should evaluate to "<cnx_time>" for leg #1 of trip #1
   Then the rule rules_min_connection_time_trip.rule_min_connection_time_before should have exactly <failures> failures for trip #1

  Examples: connections
    | end   | -> | cnx_time | failures |
    | 12:30 |    | 0:30     | 0        |
    | 12:29 |    | 0:29     | 1        |
```

**Example (Skipping Steps):**
```gherkin
Scenario Outline: skipping steps
   When <update>flight #1 is cancelled
   Then the rave variable "leg.%is_cancelled%" should evaluate to "<is_cancelled>" for leg #1

  Examples: cases
    | update | -> | is_cancelled |
    | skip:  |    | False        |
    |        |    | True         |
```

---

## 4.1.6. Test Rave Rules

### Business value of the rule
* Base test cases on business values.
* Focus on main business cases.
* Cover main cases in one Scenario Outline.

### Rule failure properties
Test attributes like:
* `leg` (which leg is blamed)
* `blametime`, `failtext`, `rule exceptable`, `severity`, etc.

```gherkin
Then the rule rules_restriction.training_restriction should evaluate the following for crewmember #1
  | leg | pass | failtext                                         | rule exceptable |
  | 1   | fail | RST 1.3: Crew active during training restriction | False           |
```

### Validity and applicability
Test if the rule applies correctly to specific contexts (e.g., cockpit vs. cabin, part-time vs. full-time).

### Alert properties
Test that the rule has the correct icon in the Alert Monitor.
```gherkin
Then the rule rules_restriction.training_restriction is in alert group union
```

---

## 4.1.7. Workflow with Jira issues

### Reporting issues
Core provides a `gherkin_report` that generates content for behave scenarios. This can be run from the Tracking Editor or command line:
```bash
report gherkin_report crew_roster <crew_alias>
```
* **Pros:** GDPR-safe, easy to reproduce, contains customer-specific attributes.
* **Cons:** May contain too much info (all times/attributes) or too little (history/annotations).

### Resolving an issue
1. Create a temporary `jira-1234.feature`.
2. Tweak until reproducible.
3. Once fixed, move relevant parts to a permanent feature file.
4. Remove irrelevant information and add descriptions.

---

## 4.1.8. Ignoring test cases

### To be fixed later
Use tags to skip failing tests and link them to a Jira:
```gherkin
@ignore @JIRA-1234
Scenario: Some very important test case
```
List all tags: `behave tags`. Run specific tags: `behave run --tags JIRA-1234`.

### Demo data
Behave can prepare data for demonstrations. Store these in an ignored folder. To persist to an existing Oracle database:
```bash
export BEHAVE_DATABASE_USE_CMSSHELL=1
behave test_suites
```

---

## 4.1.9. Write new behave steps

1. **Check existing:** See if dynamic attribute handling already covers the need.
2. **When to write:** New tables, model extensions, or new APIs/processes.
3. **Data types:** Use `AbsTime`, `RelTime`, `SeqNo`, `ValidPeriod`.
4. **Catalog data:** Do not create catalog data in steps; use `initial_load`.
5. **User-centric:** Avoid technical steps; use wording the end user sees (e.g., "When a scheduler checks in...").
6. **Consistency:** Use common ways to refer to objects.
7. **Documentation:** Document table inputs using ReST format, including mandatory/optional fields and examples.
8. **Assertions:** Use the `failtext` function for clear error messages.
9. **Self-tests:** Provide self-test feature files for new steps.
