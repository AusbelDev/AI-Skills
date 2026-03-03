## Functions

### carmensystems.rave.api.buffer2context


`carmensystems.rave.api.``buffer2context`(*buffer*)
:   Creates an anonymous Rave context given a buffer object provided by a planning application’s Python interface.

    Examples:

    ```
    eval(buffer2context(buffer), ...)

    for chain in buffer2context(buffer).bag().chain_set():
        ...
    ```

    |  |  |
    | --- | --- |
    | Parameters: | **buffer** – the buffer (representing a set of planning objects). |
    | Return type: | [`Context`](carmensystems.rave.api.Context.html#carmensystems.rave.api.Context "carmensystems.rave.api.Context") |

### carmensystems.rave.api.constraint

### carmensystems.rave.api.constraint_eval


`carmensystems.rave.api.``constraint_eval`(*where=None*, *sort\_by=None*)
:   Creates an [`Iteration`](carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") over all constraint evaluations. If applied without a context, it evaluates global constraints. If applied on a single chain, it evaluates chain-dependent (vertical) constraints. It always runs on the whole chain, never a subsequence.

    This Iteration generates [`ConstraintEval`](carmensystems.rave.api.ConstraintEval.html#carmensystems.rave.api.ConstraintEval "carmensystems.rave.api.ConstraintEval") objects as loop data (see [`foreach`](../api.html#carmensystems.rave.api.foreach "carmensystems.rave.api.foreach")). Note that returned loop data can be used to compute Rave values on the failed object, but iterators cannot be applied.

    |  |  |
    | --- | --- |
    | Parameters: | * **where** (*scalar evaluator(s)*) – filter condition, or tuple of filter conditions. Each condition must evaluate to a boolean value. Objects for which a condition fails will be skipped by the iteration. * **sort\_by** (*scalar evaluator(s)*) – a sort key, or tuple of sort keys. The iteration will sort the output by these keys, in ascending order. |
    | Return type: | [`Iteration`](carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") |

### carmensystems.rave.api.constraints


`carmensystems.rave.api.``constraints`()
:   Iterator for all constraints.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Constraint`](carmensystems.rave.api.Constraint.html#carmensystems.rave.api.Constraint "carmensystems.rave.api.Constraint")s. |

### carmensystems.rave.api.context

### carmensystems.rave.api.contexts


`carmensystems.rave.api.``contexts`()
:   Iterator for all contexts.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Context`](carmensystems.rave.api.Context.html#carmensystems.rave.api.Context "carmensystems.rave.api.Context")s. |

### carmensystems.rave.api.eval


`carmensystems.rave.api.``eval`(*\*args*)
:   Compute values for a number of *evaluator* s. First argument may optionally be a bag to use in the evaluations (see *Bag interface* ). The bag may be specified by a [`Context`](carmensystems.rave.api.Context.html#carmensystems.rave.api.Context "carmensystems.rave.api.Context") object or context name (string); the bag returned by the [`Context.bag()`](carmensystems.rave.api.Context.html#carmensystems.rave.api.Context.bag "carmensystems.rave.api.Context.bag") method will then be used.

    The *dependency level* of the evaluators must match the level given by the bag.

    |  |  |
    | --- | --- |
    | Returns: | A tuple containing the value returned from each evaluator argument, computed on the given bag (if any). |

### carmensystems.rave.api.explorer_init


`carmensystems.rave.api.``explorer_init`(*fileName*)
:   Start a new explorer session if the rule set is compiled for exploring.
    All caches, contexts and bags are also reset.

    |  |  |
    | --- | --- |
    | Parameters: | **fileName** (`string`) – Absolute path to explorer output file. |

### carmensystems.rave.api.explorer_restore


`carmensystems.rave.api.``explorer_restore`()
:   Stop explorer session.

### carmensystems.rave.api.external_table_modified


`carmensystems.rave.api.``external_table_modified`(*tableName=None*)
:   Notify Rave that an external table need to be reloaded. The table will be reloaded the next time it is accessed and only if the table is modified.

    |  |  |
    | --- | --- |
    | Parameters: | **tableName** (`string`) – Name of the table to reload. The name is the external part as defined in the Rave code. If no name is specified or name is None, all loaded modified tables will be reloaded. |

### carmensystems.rave.api.first


`carmensystems.rave.api.``first`(*level*, *computable*)
:   Creates a [`Traverser`](carmensystems.rave.api.Traverser.html#carmensystems.rave.api.Traverser "carmensystems.rave.api.Traverser") that evaluates **computable** on the first object on sub-level **level** .

    Example (using [`Level.atom()`](carmensystems.rave.api.Level.html#carmensystems.rave.api.Level.atom "carmensystems.rave.api.Level.atom")):

    ```
    # Evaluate 'departure' on the first leg of the current object:
    first(Level.atom(), 'departure')
    ```

    |  |  |
    | --- | --- |
    | Parameters: | * **level** (`string` or [`Level`](carmensystems.rave.api.Level.html#carmensystems.rave.api.Level "carmensystems.rave.api.Level")) – the sub-level. The level must be less or equal to the evaluation level. * **computable** (*scalar computable*) – what to evaluate. |
    | Return type: | [`Traverser`](carmensystems.rave.api.Traverser.html#carmensystems.rave.api.Traverser "carmensystems.rave.api.Traverser") |

### carmensystems.rave.api.global_constraint_evals


`carmensystems.rave.api.``global_constraint_evals`(*where=None*, *sort\_by=None*)
:   Iterator over global constraint evaluations. Complement to the `constraint_evals()` method in the *Bag interface* : Returns the same kind of iterator, but for global constraints. (The iterator returns (bag, [`ConstraintEval`](carmensystems.rave.api.ConstraintEval.html#carmensystems.rave.api.ConstraintEval "carmensystems.rave.api.ConstraintEval")) tuples.)

    |  |  |
    | --- | --- |
    | Parameters: | * **where** (*scalar evaluator(s)*) – filter condition, or tuple of filter conditions. Each condition must evaluate to a boolean value. Objects for which a condition fails will be skipped by the iteration. * **sort\_by** (*scalar evaluator(s)*) – a sort key, or tuple of sort keys. The iteration will sort the output by these keys, in ascending order. |
    | Returns: | A *Bag interface* iterator |

### carmensystems.rave.api.group

### carmensystems.rave.api.groups


`carmensystems.rave.api.``groups`()
:   Iterator for all groups.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Group`](carmensystems.rave.api.Group.html#carmensystems.rave.api.Group "carmensystems.rave.api.Group")s. |

### carmensystems.rave.api.iter


`carmensystems.rave.api.``iter`(*iterator\_or\_transform*, *where=None*, *sort\_by=None*)
:   Creates an [`Iteration`](carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") using a Rave iterator or transform.

    |  |  |
    | --- | --- |
    | Parameters: | * **iterator\_or\_transform** ([`Iterator`](carmensystems.rave.api.Iterator.html#carmensystems.rave.api.Iterator "carmensystems.rave.api.Iterator"), [`Transform`](carmensystems.rave.api.Transform.html#carmensystems.rave.api.Transform "carmensystems.rave.api.Transform") or `string`) – a Rave iterator or transform. * **where** (*scalar evaluator(s)*) – filter condition, or tuple of filter conditions. Each condition must evaluate to a boolean value. Objects for which a condition fails will be skipped by the iteration. * **sort\_by** (*scalar evaluator(s)*) – a sort key, or tuple of sort keys. The iteration will sort the output by these keys, in ascending order. |
    | Return type: | [`Iteration`](carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") |

### carmensystems.rave.api.iterator

### carmensystems.rave.api.iterators


`carmensystems.rave.api.``iterators`()
:   Iterator for all iterators.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Iterator`](carmensystems.rave.api.Iterator.html#carmensystems.rave.api.Iterator "carmensystems.rave.api.Iterator")s. |

### carmensystems.rave.api.keyw


`carmensystems.rave.api.``keyw`(*name*)
:   Get a reference to a [`Keyword`](carmensystems.rave.api.Keyword.html#carmensystems.rave.api.Keyword "carmensystems.rave.api.Keyword") object.

    |  |  |
    | --- | --- |
    | Parameters: | **name** (`string`) – the name of the keyword. |
    | Return type: | [`Keyword`](carmensystems.rave.api.Keyword.html#carmensystems.rave.api.Keyword "carmensystems.rave.api.Keyword") |

### carmensystems.rave.api.keywords


`carmensystems.rave.api.``keywords`()
:   Iterator for all keywords.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Keyword`](carmensystems.rave.api.Keyword.html#carmensystems.rave.api.Keyword "carmensystems.rave.api.Keyword")s. |

### carmensystems.rave.api.last


`carmensystems.rave.api.``last`(*level*, *computable*)
:   Creates a [`Traverser`](carmensystems.rave.api.Traverser.html#carmensystems.rave.api.Traverser "carmensystems.rave.api.Traverser") that evaluates **computable** on the last object on sub-level **level** .

    Example (using [`Level.atom()`](carmensystems.rave.api.Level.html#carmensystems.rave.api.Level.atom "carmensystems.rave.api.Level.atom")):

    ```
    # Evaluate 'arrival' on the last leg of the current object:
    last(Level.atom(), 'arrival')
    ```

    |  |  |
    | --- | --- |
    | Parameters: | * **level** (`string` or [`Level`](carmensystems.rave.api.Level.html#carmensystems.rave.api.Level "carmensystems.rave.api.Level")) – the sub-level. The level must be less or equal to the evaluation level. * **computable** (*scalar computable*) – what to evaluate. |
    | Return type: | [`Traverser`](carmensystems.rave.api.Traverser.html#carmensystems.rave.api.Traverser "carmensystems.rave.api.Traverser") |

### carmensystems.rave.api.level

### carmensystems.rave.api.levels


`carmensystems.rave.api.``levels`()
:   Iterator for all levels.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Level`](carmensystems.rave.api.Level.html#carmensystems.rave.api.Level "carmensystems.rave.api.Level")s. |

### carmensystems.rave.api.module

### carmensystems.rave.api.modules


`carmensystems.rave.api.``modules`()
:   Iterator for all modules.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Module`](carmensystems.rave.api.Module.html#carmensystems.rave.api.Module "carmensystems.rave.api.Module")s. |

### carmensystems.rave.api.param


`carmensystems.rave.api.``param`(*name*)
:   Get a reference to a [`Parameter`](carmensystems.rave.api.Parameter.html#carmensystems.rave.api.Parameter "carmensystems.rave.api.Parameter") object.

    |  |  |
    | --- | --- |
    | Parameters: | **name** (`string`) – the name of the parameter. Full name, including module name, is required. |
    | Return type: | [`Parameter`](carmensystems.rave.api.Parameter.html#carmensystems.rave.api.Parameter "carmensystems.rave.api.Parameter") |

### carmensystems.rave.api.parameterizedsets


`carmensystems.rave.api.``parameterizedsets`()
:   Iterator for all parameterized sets.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`ParameterSet`](carmensystems.rave.api.ParameterSet.html#carmensystems.rave.api.ParameterSet "carmensystems.rave.api.ParameterSet")s. |

### carmensystems.rave.api.parameters


`carmensystems.rave.api.``parameters`()
:   Iterator for all parameters.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Parameter`](carmensystems.rave.api.Parameter.html#carmensystems.rave.api.Parameter "carmensystems.rave.api.Parameter")s. |

### carmensystems.rave.api.paramset


`carmensystems.rave.api.``paramset`(*name*)
:   Get a reference to a [`ParameterSet`](carmensystems.rave.api.ParameterSet.html#carmensystems.rave.api.ParameterSet "carmensystems.rave.api.ParameterSet") object.

    |  |  |
    | --- | --- |
    | Parameters: | **name** (`string`) – the name of the set. Full name, including module name, is required. |
    | Return type: | [`ParameterSet`](carmensystems.rave.api.ParameterSet.html#carmensystems.rave.api.ParameterSet "carmensystems.rave.api.ParameterSet") |

### carmensystems.rave.api.profiler_init


`carmensystems.rave.api.``profiler_init`()
:   Start a profiler session if the rule set is compiled for profiling.

### carmensystems.rave.api.profiler_reset


`carmensystems.rave.api.``profiler_reset`(*profileName=None*, *timeStamp=True*)
:   Terminate the Rave profiler session and optionally save collected
    profiler data to an XML file.

    |  |  |
    | --- | --- |
    | Parameters: | * **profileName** (`string`) – Name of the XML data file to save.  File type suffix (.xml) is added automatically.   The XML file is saved in the $CARMTMP/RaveProfiling directory.   Calling the function without `profileName` parameter will terminate   the profiling session without saving data to file. * **timeStamp** ((convertible to) `bool`) – If `True`, add a timestamp to the file name. |

### carmensystems.rave.api.profiler_save


`carmensystems.rave.api.``profiler_save`(*profileName*, *timeStamp=True*)
:   Save the collected profiler data to an XML file

    |  |  |
    | --- | --- |
    | Parameters: | * **profileName** (`string`) – Name of the XML data file to save.  File type suffix (.xml) is added automatically.   The XML file is saved in the $CARMTMP/RaveProfiling directory.   Calling the function when no profiling session is running will have   no effect. * **timeStamp** ((convertible to) `bool`) – If `True`, add a timestamp to the file name. |

### carmensystems.rave.api.profiler_start


`carmensystems.rave.api.``profiler_start`()
:   Start the Rave profiler performance measurement if a profiler
    session is running.

### carmensystems.rave.api.profiler_status


`carmensystems.rave.api.``profiler_status`()
:   Return 2-tuple with profiler status (one of the `PROFILER_*` constants) and data quality (integer).

    |  |  |
    | --- | --- |
    | Return type: | tuple |

### carmensystems.rave.api.profiler_stop


`carmensystems.rave.api.``profiler_stop`()
:   Stop/pause the Rave profiler performance measurement if a profiler
    session is running.

### carmensystems.rave.api.rule

### carmensystems.rave.api.rulefailure


`carmensystems.rave.api.``rulefailure`(*where=None*, *sort\_by=None*, *group=None*)
:   Creates an [`Iteration`](carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") over all rule failures on the current chain. It always runs on the whole chain, never a subsequence.

    This Iteration generates [`RuleFail`](carmensystems.rave.api.RuleFail.html#carmensystems.rave.api.RuleFail "carmensystems.rave.api.RuleFail") objects as loop data (see [`foreach`](../api.html#carmensystems.rave.api.foreach "carmensystems.rave.api.foreach")). Note that returned loop data can be used to compute Rave values on the failed object, but iterators cannot be applied.

    |  |  |
    | --- | --- |
    | Parameters: | * **where** (*scalar evaluator(s)*) – filter condition, or tuple of filter conditions. Each condition must evaluate to a boolean value. Objects for which a condition fails will be skipped by the iteration. * **sort\_by** (*scalar evaluator(s)*) – a sort key, or tuple of sort keys. The iteration will sort the output by these keys, in ascending order. * **group** ([`Group`](carmensystems.rave.api.Group.html#carmensystems.rave.api.Group "carmensystems.rave.api.Group") or `string`) – if specified, only rules belonging to this group will be checked. |
    | Return type: | [`Iteration`](carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") |

### carmensystems.rave.api.rules


`carmensystems.rave.api.``rules`()
:   Iterator for all rules.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Rule`](carmensystems.rave.api.Rule.html#carmensystems.rave.api.Rule "carmensystems.rave.api.Rule")s. |

### carmensystems.rave.api.ruleset_loaded


`carmensystems.rave.api.``ruleset_loaded`()
:   |  |  |
    | --- | --- |
    | Returns: | `True` if a ruleset is loaded, `False` otherwise. |
    | Return type: | [bool](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)") |

### carmensystems.rave.api.selected


`carmensystems.rave.api.``selected`(*level*)
:   Creates a context containing a single level object: the one selected in the application.

    |  |  |
    | --- | --- |
    | Parameters: | **level** ([`Level`](carmensystems.rave.api.Level.html#carmensystems.rave.api.Level "carmensystems.rave.api.Level") or `string`) – the level to use. Const level is not accepted. |
    | Return type: | [`Context`](carmensystems.rave.api.Context.html#carmensystems.rave.api.Context "carmensystems.rave.api.Context") |

### carmensystems.rave.api.set

### carmensystems.rave.api.sets


`carmensystems.rave.api.``sets`()
:   Iterator for all sets.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Set`](carmensystems.rave.api.Set.html#carmensystems.rave.api.Set "carmensystems.rave.api.Set")s. |

### carmensystems.rave.api.times


`carmensystems.rave.api.``times`(*num*, *where=None*, *sort\_by=None*)
:   Creates an iteration that runs **num** times

    |  |  |
    | --- | --- |
    | Parameters: | * **num** (*scalar evaluator*) – the number of times to iterate. * **where** (*scalar evaluator(s)*) – filter condition, or tuple of filter conditions. Each condition must evaluate to a boolean value. Objects for which a condition fails will be skipped by the iteration. * **sort\_by** (*scalar evaluator(s)*) – a sort key, or tuple of sort keys. The iteration will sort the output by these keys, in ascending order. |
    | Return type: | [`Iteration`](carmensystems.rave.api.Iteration.html#carmensystems.rave.api.Iteration "carmensystems.rave.api.Iteration") |

### carmensystems.rave.api.transform

### carmensystems.rave.api.transforms


`carmensystems.rave.api.``transforms`()
:   Iterator for all transforms.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Transform`](carmensystems.rave.api.Transform.html#carmensystems.rave.api.Transform "carmensystems.rave.api.Transform")s. |

### carmensystems.rave.api.var


`carmensystems.rave.api.``var`(*name*)
:   Get a reference to a [`Variable`](carmensystems.rave.api.Variable.html#carmensystems.rave.api.Variable "carmensystems.rave.api.Variable") object.

    |  |  |
    | --- | --- |
    | Parameters: | **name** (`string`) – the name of the variable. Full name, including module name, is required. |
    | Return type: | [`Variable`](carmensystems.rave.api.Variable.html#carmensystems.rave.api.Variable "carmensystems.rave.api.Variable") |

### carmensystems.rave.api.variables


`carmensystems.rave.api.``variables`()
:   Iterator for all variables.

    |  |  |
    | --- | --- |
    | Returns: | definition iterator with [`Variable`](carmensystems.rave.api.Variable.html#carmensystems.rave.api.Variable "carmensystems.rave.api.Variable")s. |