## Groups

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.11.html)  | [next](Definitions.06.13.html) |

> Groups
>
> Rave groups make it possible to organize parameters and other definitions in a rule set into groups or classes. During run time, groups can be used to present chosen subsets of parameters or validate subsets of rules.
>
> The definitions that can be grouped are: rules, internal sets, parameters and constraints. The syntax of a group definition is:
>
> |  |  |  |
> | --- | --- | --- |
> | group\_def | ::= | group group\_ident = [groupmems] [remark]; |group group\_ident [remark] ; |
> | group\_ident | ::= | ident |
> | groupmems | ::= | groupmems , groupmem |groupmem |
> | groupmem | ::= | qual\_ident |
>
> Thegroup\_ident is the name of the group and the groupmems are names of definitions. Group members must be unique within a group and duplicates are silently deleted. A definition can belong to more than one group, and it can also be added to or removed from a group during run time.
>
> |  |  |
> | --- | --- |
> | Example 1 | %parA% = parameter 1; %parB% = parameter 2; %parXYZ% = parameter 3; |
> |  | group grpA = %parA%,%parXYZ%; group grpB = %parB%,%parXYZ%; |
> |  | This example shows three parameters that are organized into two groups. When this rule set is loaded,%parA% will belong to group grpA, %parB% will belong to grpB and %parXYZ% will belong to both groups. |
>
> The group definition is additive. If you define the same group in several places, the resulting group contains all the group members in the different group definitions.
>
> |  |  |
> | --- | --- |
> | Example 2 | group test = rule1; group test = rule2;  In this example, thetest group contains both rule1 and rule2. |
>
> If you redefine a group, you can use a place holder to keep the group members in the parent group. See[Multiple implementations](Modules.07.3.html#22029 "Multiple implementations").

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.11.html)  | [next](Definitions.06.13.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |