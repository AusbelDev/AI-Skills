## Accumulators

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.12.html)  | [next](Definitions.06.14.html) |

> Accumulators
>
> Accumulators enable a Rave programmer to approximately model rules spanning over longer time periods, both historical and future, than the currently loaded plan. An accumulator is typically used for a crew member property like duty time or events like medical checks. Accumulators can be defined for sums of Int and Reltime values, as well as for Abstime points.
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Syntax](#65534 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Attributes](#35408 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Accumulator result](#67725 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Dependency](#65187 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Storage](#37106 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Update program](#39100 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Reltime accumulator example](#39287 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Abstime accumulator example](#39885 "Accumulators") |
>
> |  |  |
> | --- | --- |
> | • | [Abstime accumulator using acc\_filter](#39202 "Accumulators") |
>
> Syntax
>
> The accumulator syntax is as follows:
>
> |  |  |  |
> | --- | --- | --- |
> | accumulator | ::= | gexportaccumulator acc\_ident (formal\_args) =    expression ;    [iterator = iter\_ident ;]    (attribute)\*  end |
> | acc\_ident | ::= | ident |
> | attribute | ::= | attr\_ident [(formal\_args)] = expression ; |external expression ; |
> | attr\_ident | ::= | ident |
>
> For Int and Reltime accumulators, the formal arguments must be an interval given by two Abstime time points: thestart and end arguments. For an Abstime accumulator, the first argument must be an Abstime time point, the start argument, and the second argument a Bool direction argument (forward = true, backward = false).
>
> In Rave you refer to the value of an accumulator by calling the accumulator like a function:
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | acc\_ident (expr, expr) |
>
> Expression
>
> In an accumulator definition, the expression specifies how the accumulator's value is computed on data in the loaded plan. Thus, when defining the expression you should assume that the data is available.
>
> For an Int or a Reltime accumulator, the expression should calculate the contribution from the loaded plan in the interval specified by the formal arguments. The values of the formal arguments are adjusted automatically depending on theplan\_start, plan\_end, and stored time points and may form a sub-interval of the input interval. See [Accumulator result](#67725 "Accumulators") for details. If the resulting interval is empty, that is if the start time is greater than or equal to the end time, the contribution should be zero (0 or 0:00). A sub-interval of an interval must not result in a larger contribution than the original interval.
>
> For an Abstime accumulator, the expression should result in a time point that depends on the givenstart and direction arguments. The direction argument is either true or false for forward and backward respectively, and the result should be a valid time point t according to:
>
> |  |  |
> | --- | --- |
> | • | forward: smallestt such that start <= t < plan\_end |
>
> |  |  |
> | --- | --- |
> | • | backward: largestt such that plan\_start <= t <=start |
>
> If there is no such time point, the result should bevoid(Abstime). The expression should not result in a time point outside the loaded plan.
>
> Attributes
>
> The following attributes are available:
>
> |  |  |  |
> | --- | --- | --- |
> | Attribute name | Datatype | Dependency |
> | key | any datatype | chain or same as the iterator, if any |
> | plan\_start | Abstime | >= key |
> | plan\_end | Abstime | >= key |
> | proj\_interval\_func | Int or Reltime | >= key |
> | acc\_start | Abstime | const |
> | acc\_end | Abstime | const |
> | acc\_next(Abstime) | Abstime | const |
> | acc\_filter | Abstime | const |
> | acc\_force\_store(Abstime) | Abstime | const |
> | external | String | const |
>
> Attributes can be specified in any order, but there can be only one of each.
>
> key
>
> Thekey attribute is used to identify saved accumulated rows. It is optional if an iterator is specified, in which case the iterator partition key is used to identify the table rows if no key is given. The key expression can be of any type, but if the type is not String the values are converted to strings before written to the accumulator table.
>
> plan\_start, plan\_end
>
> Theplan\_start and plan\_end attributes define the start and end of the loaded plan and divide the input interval into three consecutive sub-intervals:
>
> |  |  |
> | --- | --- |
> | 1. | Left ofplan\_start: saved data before the plan |
>
> |  |  |
> | --- | --- |
> | 2. | Betweenplan\_start and plan\_end: the plan itself |
>
> |  |  |
> | --- | --- |
> | 3. | Right ofplan\_end: saved data after the plan |
>
> The accumulator looks up values before and after the plan in an accumulator table. The value from the plan is calculated with the accumulator expression.
>
> |  |  |
> | --- | --- |
> | Note | Theplan\_start and plan\_end attributes must be used together. The Rave compiler does not complain if none of them are defined, but in that case the accumulator acts as a function and does not look up anything in the table. |
>
> proj\_interval\_func
>
> Theproj\_interval\_func attribute is an optional function. It has slightly different meaning for the different types of accumulators.
>
> For an Int or a Reltime accumulator, theproj\_interval\_func function should predict the future in a final interval between the last used data point and the end argument time point. The definition of the function should use the formal arguments of the accumulator, which are adjusted to this interval automatically. See [Accumulator result](#67725 "Accumulators") for details.
>
> For an Abstime accumulator, theproj\_interval\_func function should result in a time point at or beyond the start argument if the direction argument is True, that is, forward. Otherwise, it should result in a time point before or at the start argument. In both cases, it may also return void(Abstime) to indicate no time point. This function is only called if no other time points are found from the plan or the accumulator table.
>
> acc\_start, acc\_end, acc\_next
>
> Theacc\_start, acc\_end, and acc\_next attributes define the interval and resolution of the accumulation process. That is, they are only used when data is collected from the loaded plan and saved as samples in the accumulator table.
>
> Theacc\_start attribute specifies the starting point of the accumulation. For Int and Reltime accumulators, the value of the attribute is not used directly but filtered through the acc\_next(acc\_start - 0:01) expression. This is to take advantage of any rounding in the acc\_next(Abstime t) function.
>
> Theacc\_end attribute specifies where the accumulation should end. The end point itself is not included.
>
> Theacc\_next(Abstime t) function should only be specified for Int and Reltime accumulators. This attribute receives the previous time point and should return the time point for the next sample. For example, to collect one sample per day, just add 24:00. Do not define this function for Abstime accumulators.
>
> acc\_filter
>
> Theacc\_filter attribute can be used for Abstime accumulators. It populates the filt column in the accumulator\_time table, see [Storage](#37106 "Accumulators"), with a value that can be used for filtering.
>
> acc\_force\_store
>
> Theacc\_force\_store attribute can be used for Int and Reltime accumulators. It forces storage of specific time points, for example January 1 each year.
>
> external
>
> Theexternal attribute specifies an external table where to store and read accumulated values. The same table may be used for more than one accumulator of the same type, but accumulators with different main expression data types must use different tables. The specified table must exist and have the following columns:
>
> |  |  |
> | --- | --- |
> | • | name of type String |
>
> |  |  |
> | --- | --- |
> | • | acckey of type String |
>
> |  |  |
> | --- | --- |
> | • | tim of type Abstime |
>
> |  |  |
> | --- | --- |
> | • | val of type Int or Reltime, depending on the type of the main accumulator expression. This field should be omitted for Abstime accumulators. |
>
> If this optional attribute is not specified, the default system tables for Int, Reltime, and Abstime accumulators are used. See[Storage](#37106 "Accumulators"). The attribute can be useful, for example, for performance reasons.
>
> |  |  |
> | --- | --- |
> | Note | Accumulators with the same name that appear in more than one rule set in a super rule set must have the same value on theexternal attribute. |
>
> If accumulators with the same name appear in more than one rule set in a super rule set and only some of them specify theexternal attribute, then the attribute value must be one of he default table names (accumulator\_int, accumulator\_rel or accumulator\_time).
>
> Accumulator result
>
> The result of an accumulator is calculated differently depending on its type.
>
> Int and Reltime
>
> The result of a call to an Int or Reltime accumulatoracc with the interval [b, e), acc(b, e), is evaluated by first deciding the following time points:
>
> |  |  |
> | --- | --- |
> | • | t0 = min(t), where t >= b and t is a stored value |
>
> |  |  |
> | --- | --- |
> | • | t1 = max(t), where t <= acc.plan\_start and t is a stored value |
>
> |  |  |
> | --- | --- |
> | • | t2 = min(t), where t >= acc.plan\_end and t is a stored value |
>
> |  |  |
> | --- | --- |
> | • | t3 = max(t), where t <= e and t is a stored value |
>
> |  |  |
> | --- | --- |
> | • | t4 = e |
>
> Ift0 to t3 are all stored in the table, the result of the call is the sum of:
>
> tab[t1] - tab[t0]  
> acc.expr(t1, t2)  
> tab[t3] - tab[t2]  
> acc.proj\_interval\_func(t3, t4)
>
> where:
>
> tab[t]
>
> the value stored in the tableacc.external[acc.name, acc.key, t].
>
> acc.expr(t1, t2)
>
> the value of the accumulator expression with its formal arguments set tot1 and t2.
>
> acc.proj\_interval\_func(t3, t4)
>
> the value of the projection function, if existing, with the accumulator's formal arguments set tot3 and t4.
>
> Otherwise, ifb >= plan\_start or there is no t0 or t1 stored in the table, then t1 = b and the contribution of the first term is zero.
>
> Likewise, ife <= plan\_end or there is no t2 or t3 stored in the table, then t2 = t3 = plan\_end and the contribution of the third term is zero.
>
> Abstime
>
> The result of a call to an Abstime accumulatoracc with the arguments start and direction, acc(start, direction), is evaluated according to:
>
> direction=True (forward):
>
> |  |  |
> | --- | --- |
> | 1. | plan\_end <= startIf the start argument is after the plan, the time point is looked up in the accumulator table and the result is the smallest time point t such that start <= t. If no time point is found, the result is void(Abstime). |
>
> |  |  |
> | --- | --- |
> | 2. | plan\_start <= start < plan\_endIf the start argument is within the plan, the result is the evaluation of the accumulator expression. Should the expression be void, a table lookup according to point 1 is done instead, with the value of the plan\_end attribute as the value of the start argument. Note that the evaluated time point is not automatically restricted to the plan interval. |
>
> |  |  |
> | --- | --- |
> | 3. | start < plan\_start  If the start argument is before the plan, the time point is looked up from the accumulator table and the result is the smallest time point t such that start <= t < plan\_start. If no such time point is found, the accumulator expression in point 2 is used instead, with the value of the plan\_start attribute as the value of the start argument. |
>
> direction=False (backward):
>
> |  |  |
> | --- | --- |
> | 1. | start < plan\_start  If the start argument is before the plan, the time point is looked up from the accumulator table. The result is the largest time point that is less than or equal to start, or void(Abstime) if no such time point exists. |
>
> |  |  |
> | --- | --- |
> | 2. | plan\_start <= start < plan\_end  If the start argument is within the plan, the result is the evaluation of the accumulator expression. Should the expression be void, a table lookup according to point 1 is done instead, with the value of the plan\_start attribute as the value of the start argument. Note that the evaluated time point is not automatically restricted to the plan interval. |
>
> |  |  |
> | --- | --- |
> | 3. | plan\_end <= start  If the start argument is after the plan, the time point is looked up in the accumulator table and the result is the largest time point t such that plan\_end <= t <= start. If no such time point is found, the accumulator expression in point 2 is used instead, with the value of the plan\_end attribute as the value of the start argument. |
>
> Dependency
>
> The dependency of an accumulator is the greatest common dependency of its main expression's dependency, the dependency of the referred iterator, if any, and all the attributes' dependencies.
>
> If both a key is defined and an iterator is referred, they must have the same dependency. If no iterator is defined, the dependency of the accumulator must be chain or constant. If akey is defined, its dependency must be dominated by the accumulator dependency.
>
> The dependencies of theacc\_start, acc\_end, and acc\_next attributes must all be constant.
>
> Storage
>
> Accumulator values are stored in external tables. By default there is one table for each data type of the accumulator value, named according to:
>
> |  |  |
> | --- | --- |
> | Etable name | Datatype |
> | accumulator\_int | Int |
> | accumulator\_rel | Reltime |
> | accumulator\_time | Abstime |
>
> Each external table has the following columns:.
>
> |  |  |  |
> | --- | --- | --- |
> | Column name | Datatype | Comment |
> | name | String | Accumulator name |
> | acckey | String | Partition key or object identifier |
> | tim | Abstime | End of period (Int and Reltime accumulators)  Time point (Abstime accumulator) |
> | val | Int or Reltime | Int and Reltime accumulators only |
> | filt | Abstime | Only used with theacc\_filter attribute (Abstime). |
>
> The accumulator tables must exist. Rave does not create new external tables.
>
> You can also specify other external tables for storage by using theexternal attribute. See [Attributes](#35408 "Accumulators").
>
> Int and Reltime
>
> In an Int or Reltime accumulator table, eachval specifies how much is accumulated up to, but not including, the time point tim for an accumulator named name and an object identified by acckey.
>
> |  |  |  |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | Example | An accumulator collects time from a roster and saves one sample every midnight. Consider a roster containing three legs with the following times:  |  |  | | --- | --- | | • | Dec 12 21:55 - Dec 13 00:01 |  |  |  | | --- | --- | | • | Dec 13 10:00 - Dec 13 14:00 |  |  |  | | --- | --- | | • | Dec 13 23:58 - Dec 14 01:30 |  The new sample for Dec 14 is 0:01 + 4:00 + 0:02 = 4:03 larger than the previous sample. If the accumulated value for Dec 13 is 100:00, the new sample for Dec 14 is 100:00 + 4:03 = 104:03. To retrieve the accumulated time for the whole of Dec 13, subtract table[Dec 14].val - table[Dec 13].val = 104:03 - 100:00 = 4:03. For this to work correctly, the mapping fromtim to val must be monotonic. That is, the value may only increase, or only decrease, from sample to sample. |
>
> Two consecutive intervals that both contribute with 0 or 0:00 give three consecutive samples with the same values. If this happens, the middle sample is left out. This does not affect the difference value fetched from the table, but it might affect the time points for found samples which in turn may affect the result from the accumulator expression and/or theproj\_interval\_func function, see [Accumulator result](#67725 "Accumulators").
>
> Abstime
>
> An Abstime accumulator table lacks theval column, since it does not associate time points with values but just stores time events. The time points themselves are the results of Abstime accumulators.
>
> Update program
>
> Accumulators are supposed to be updated periodically or manually by an update program in the application.
>
> Reltime accumulator example
>
> The following example is for an accumulator that returns the accumulated block time for a crew member between two time points,s and e, where s < e.
>
> Theacc\_end value in the example extends the accumulation interval by an extra minute (since acc\_end is defined as not being part of the interval).
>
> |  |  |
> | --- | --- |
> | Example 1 | accumulator block\_acc(Abstime s, Abstime e) =    sum(leg(roster), %block\_time%)        where (arrival > s and arrival <= e);    key = crr\_crew\_id;    plan\_start = pp.%start%;    plan\_end = pp.%end%;    proj\_interval\_func = (e-s)/5;    acc\_start = round\_down(pp.%start%, 24:00);    acc\_end = pp.%end% + 0:01;    acc\_next(Abstime t) = t+24:00; end |
>
> Example 2 shows how the accumulator can be used in a rule.
>
> |  |  |
> | --- | --- |
> | Example 2 | rule max\_block\_in\_28days =    valid %is\_on\_duty%;    block\_acc(leg.%start\_day% - 28\*24:00,              leg.%start\_day%) <= 120:00;    remark "Maximum 120 block hours in 28 days"; end |
>
> Abstime accumulator example
>
> Theacc\_last\_extended\_dh accumulator keeps track of extended deadhead trips.
>
> |  |  |
> | --- | --- |
> | Example 1 | accumulator acc\_last\_ext\_dh(Abstime starttime, Bool forward) =     if forward then         first(trip(chain), trip.%end\_hb%)         where (trip.%start\_hb% >= starttime                and trip.%is\_ext\_deadhead%)     else         last(trip(chain), trip.%end\_hb%)         where(trip.%start\_hb% <= starttime               and trip.%is\_ext\_deadhead%);     key = crr\_crew\_id;     acc\_start = %pp\_start%;     acc\_end = %pp\_end% + 0:01; end |
>
> This accumulator can be used in a rule to ensure that an extended deadhead trip starts at least three months after the end of the previous extended deadhead trip.
>
> |  |  |
> | --- | --- |
> | Example 2 | rule 3\_months\_btw\_extended\_dh =     valid roster.%check\_rules%         and trip.%is\_ext\_deadhead%;     trip.%start\_hb% >= add\_months(         acc\_last\_ext\_dh(trip.%start\_hb%, false), 3);     remark "At least three months between extended deadheads"; end |
>
> Abstime accumulator using acc\_filter
>
> This accumulator populates thefilt column in accumulator\_time with the next deadhead arrival time.
>
> |  |  |
> | --- | --- |
> | Example | accumulator last\_dh(abstime starttime, bool forward) =     if forward then         first(leg(chain), arrival)         where(arrival > starttime and deadhead)     else         last(leg(chain), arrival)         where(arrival < starttime and deadhead);     key = crr\_crew\_id;     acc\_start = %pp\_start% + (if forward then 0:00 else 0:01);     acc\_end = %pp\_end% + 0:01;     acc\_filter = first(leg(chain), next(leg(chain), arrival))                  where(arrival > starttime and deadhead); end |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.12.html)  | [next](Definitions.06.14.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |