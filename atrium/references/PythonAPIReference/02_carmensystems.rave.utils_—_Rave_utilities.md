# carmensystems.rave.utils — Rave utilities


This module provides Rave-related utilities.

### Functions

Rave API Utilities

`carmensystems.rave.utils.``eval_accumulators`(*ApplicationBuffer=None*, *from=None*, *to=None*)
:   Evaluates all accumulators in the loaded Rave program.

    If no ‘ApplicationBuffer’ is given, the current default context is used.
    If no ‘from’ and ‘to’ times are given, acc\_start and acc\_end as defined in the
    Rave program are used.

    Example:

    ```
    import carmensystems.rave.utils as rave_utils
    rave_utils.eval_accumulators()
    ```

    See the Rave reference manual for more information about accumulators.

    |  |  |
    | --- | --- |
    | Parameters: | * **ApplicationBuffer** (*ApplicationBuffer* *or* [*Context*](stubs/carmensystems.rave.api.Context.html#carmensystems.rave.api.Context "carmensystems.rave.api.Context")) – a Rave buffer or context * **from** ([*AbsTime*](../basics/abstime.html#AbsTime.AbsTime "AbsTime.AbsTime")) – accumulation start time point * **to** ([*AbsTime*](../basics/abstime.html#AbsTime.AbsTime "AbsTime.AbsTime")) – accumulation stop time point |

`carmensystems.rave.utils.``eval_selected_accumulators`(*accNames*)
:   Evaluates the accumulators given as argument.
    The accumulators must exist in the loaded Rave program.

    Example:

    ```
    import carmensystems.rave.utils as rave_utils
    rave_utils.eval_selected_accumulators(['accumulators.actual_duty_time_fc_fg_acc',
                                           'accumulators.extended_duties_acc'])
    ```

    Calling the function with an empty list (‘[]’) as argument returns nothing. The function ends silently without affecting anything.

    A RuntimeError is raised if

    > * the function is called without any argument.
    > * the function is called with non-strings in the list.
    > * the function is called with non-existing accumulators in the list.

    These checks are done before the accumulation begins, and no data is touched.

    |  |  |
    | --- | --- |
    | Parameters: | **accNames** – a list of qualified names of accumulators to be evaluated |
