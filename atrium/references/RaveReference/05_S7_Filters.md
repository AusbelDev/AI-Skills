## Filters

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.07.html)  | [next](Definitions.06.09.html) |

> Filters
>
> You can use filters to gain more control over data that the rules act upon. Filters make it possible to access special categories of data with a traverser, for example data concerning non-flying activities, such as free days. Filters can be regarded as a handy syntax for thewhere construct of traversers.
>
> Defining and using filters
>
> Filters provide a convenient way to filter objects on a certain traverser level, making only the currently applicable objects visible to traversers. For instance, when defining variables and rules concerning free days, the objects relating to flying activities are of no interest and it would be much easier to write the definitions if these objects were not visible to the rules.
>
> The syntax of a filter is:
>
> |  |  |  |
> | --- | --- | --- |
> | filter\_def | ::= | gexport filter filter\_ident = qual\_level\_ident ( expr ) ; |
> | filter\_ident | ::= | ident |
>
> Thefilter\_ident is the name of the filter. It can be used in traversers instead of the ordinary levels. The expression is a boolean expression.
>
> |  |  |
> | --- | --- |
> | Example 1 | filter my\_filter = leg( not deadhead );  The filtermy\_filter may replace the level leg in any expression using a traverser where only non-passive flights are interesting. The result of a traverser that uses my\_filter will never include a contribution that relates to a leg object where the keyword deadhead is true. A traverser that uses my\_filter instead of leg, ignores the deadhead objects when it obtains the next, previous, first or the last leg object. |
>
> |  |  |
> | --- | --- |
> | Example 2 | filter f\_days =  duty( first(leg(duty),activity\_type) = "F" ); |
> |  | filter r\_days =   duty( first(leg(duty),activity\_type) = "LEG" ); |
> |  | %number\_of\_free\_days% =   count(f\_days(trip)); |
> |  | %flying\_time% =    sum(r\_days(trip), sum(leg(duty),arrival-departure)); |
> |  | Assuming that the keywordactivity\_type returns the string "F" on free days and "LEG" on production days, f\_days filters everything but free days and r\_days filters everything but real duties. Consequently, the variable %number\_of\_free\_days% returns the number of free days of the current trip object and %flying\_time% returns the flying time of the rotation (a trip object) but it will skip everything that has to do with free days. |
>
> |  |  |
> | --- | --- |
> | Example 3 | An example with traversers: |
> |  | filter active\_leg =    leg( not deadhead ); |
> |  | %start1% =   first(active\_leg(duty), departure); |
> |  | %rest1% =   next(active\_leg(duty), departure) - arrival; |
> |  | active\_leg filters deadhead activities. Consequently, %start1% returns the departure time of the first non-deadhead activity of the current duty object and %rest1% returns the time between the arrival of the current activity and the departure of the next non-deadhead activity. |
> |  | Note that the condition in the filter definition must have the same dependency (be defined on the same level) as the filter itself. For instance, the following example is not correct since the filter is defined as a duty filter but the dependency of the condition is leg. |
> |  | /\* An incorrect filter definition \*/ filter foo = duty( activity\_type = "LEG" ); |
> |  | Furthermore, it is not permitted to define a filter in terms of itself.  /\* Another incorrect filter definition \*/ filter bar = leg( next(bar(duty), deadhead) ); |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.07.html)  | [next](Definitions.06.09.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |