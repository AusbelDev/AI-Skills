## Iterators and contexts

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.09.html)  | [next](Expressions.05.11.html) |

> Iterators and contexts
>
> An expression is always computed in an environment of objects, for example chains, trips, duties or legs. The contents of that environment can be affected by means of iterators, contexts and transforms.
>
> |  |  |
> | --- | --- |
> | • | Iterators are used in reports to divide a group of objects into sub-groups. All objects in a sub-group are equal in certain aspects, defined by iterator keys in the iterator definition. Most iterators are defined in the Rave language (see[Built-in iterators](#22698 "Iterators and contexts") and [Iterators](Definitions.06.10.html#23487 "Iterators")), which means that users can add iterators and modify existing ones. |
>
> |  |  |
> | --- | --- |
> | • | Contexts are used in expressions and reports to switch to another group of objects than the initial one. All contexts are predefined and not modifiable by the user. |
>
> Iterators can be used as traverser keys:
>
> |  |  |  |
> | --- | --- | --- |
> | trav\_key | ::= | qual\_iterator\_ident |
>
> Iterators can only be used together with traversers that are order-independent:sum, avg, max, min, all, any, and count. The while, from or to statements are not allowed since they require an ordered set.
>
> |  |  |
> | --- | --- |
> | Example 1 | Iterator: The number of long sectors. |
> |  | %number\_of\_long\_legs% =    count(leg\_set) where (%block% > 10:00); |
> |  | The iteratorleg\_set divides all objects of the environment into sub-groups. In this case, each single leg will form a group, due to the definition of the leg\_set iterator. count(leg\_set) counts the number of sub-groups. Since each group contains only one leg, the result will be the number of legs in the environment. The where statement makes sure that only sub-groups that fulfil the criteria of the statement are considered in the counting. A sub-group is regarded to fulfil the criteria if a single arbitrary object of the sub-group fulfils the criteria. |
>
> Contexts can also be used in expressions:
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | context ( context , expr ) |
>
> |  |  |
> | --- | --- |
> | Example 2 | Context: The number of long legs in the sub-plan. |
> |  | %number\_of\_long\_legs% =    context(sp\_crrs,      count(leg\_set) where (%block% > 10:00)); |
> |  | Example 1 did not consider the environment in which the calculation was made. The available legs were picked and the iterator divided them into groups. This example explicitly states that the calculation always must be done in an environment defined by the sp\_crrs context: the legs of all trips in the sub-plan. |
>
> Built-in iterators
>
> Rave has the following built-in iterators:
>
> above(N)
>
> Returns the iteration groupN steps above the current group. N can be any integer expression.
>
> atom\_set
>
> Theatom\_set iterator partitions each atom into a separate group.
>
> times(N)
>
> The iteration will be repeatedN times and N can be any integer expression. The active count [1-N] is available with the function times\_index.
>
> |  |  |
> | --- | --- |
> | Example 1 | %bid\_cost% = sum(times(%number\_of\_bids%),              %crew\_bid\_cost%(times\_index(0))); |
>
> Unlike other iterators, thetimes iteration is ordered. As a consequence it is allowed to use the times iterator with:  
> - a while statement  
> - the first traverser in combination with a where statement  
> - the cat traverser.
>
> actual\_leg\_period  
> actual\_chain\_period
>
> Theactual\_leg\_period and actual\_chain\_period iterators create iteration groups representing periods in which legs/chains depart on days with uniform frequency.
>
> The day frequency is uniform if the pattern of days is repeated over a 7-day week. Each day can contain one or more legs/chains.
>
> |  |  |  |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | Example 2 | Each number represents a leg/chain with the specified departure day of a week. | | | | | | |
> |  | W1 2,5  2,3,5 | W2 2,5 | W3 1,5 2,3,5 | W4 1,5,7 2,5 | W5 1,7 | => => | {2,5} {1,5} {1,7} {2,3,5} {2,3,5} {5} |
> |  | The departure of a leg is calculated with thedeparture keyword. The departure of a chain is the same as the departure of the first leg in the chain. | | | | | | |
>
> chain\_set
>
> Thechain\_set iterator partitions each chain into a separate group.
>
> crr\_period\_interval
>
> Thecrr\_period\_interval iterator creates iteration groups representing trip periods. The trip period iteration groups are defined so that no periods intersect each other. This means that new trip periods will be created if any two trip periods otherwise would intersect. Therefore one chain may belong to many groups. Below are two examples of how two trips can be divided in two periods.
>
> |  |  |  |
> | --- | --- | --- |
> | Trips | Trip periods | Resulting iteration groups |
> | t1 | 1-5 | {1-3: t1} {3-5: t1,t2} {5-7: t2} |
> | t2 | 3-7 |
> | ======================================================== | | |
> | t1 | 2-3, 6-7 | {1-2: t2} {2-3: t1,t2} {3-6: t2} {6-7: t1,t2} |
> | t2 | 1-7 |
>
> The trip periods for a specific trip are defined by thecrr\_period\_start\_N and crr\_period\_end\_N keywords.
>
> The built-in functionsinterval\_start and interval\_end may be used inside a crr\_period\_interval iteration to find the current interval, and return void if they are used outside an interval group.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.09.html)  | [next](Expressions.05.11.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |