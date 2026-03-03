## Transforms

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.10.html)  | [next](Expressions.05.12.html) |

> Transforms
>
> Transforms are used in expressions to traverse level objects of other chains that are related to the current leg or chain in some way. The set of available transforms and the way chains are related to each other are predefined by the application.
>
> A transform can be used with any order-independent traverser (sum, avg, max, min, all, any and count).
>
> Transforms are specified in two ways. An advanced transform is powerful but time consuming. It returns a group of objects (an iteration group) that can be traversed with an iterator. A simple traverser does not create any explicit groups of objects and is faster since this gives less overhead. It is recommended to try a simple traverser as the first choice.
>
> Syntax
>
> The advanced syntax is:
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | transform (    transform\_ident , trav\_ident ( group ) ) |
>
> The simple syntax is:
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | trav\_ident ( transform\_ident ) |
>
> |  |  |
> | --- | --- |
> | Example 1 | transform(ac\_rotations\_ref, count(leg\_set)) corresponds to count(ac\_rotations\_ref). |
>
> |  |  |
> | --- | --- |
> | Example 2 | %assigned\_crew% =   count(equal\_legs) where (not void(crr\_crew\_id)) |
> |  | The transformequal\_legs returns all legs belonging to the same flight as the active leg and the Example 1 counts the ones that have been assigned to any crew. |
>
> |  |  |
> | --- | --- |
> | Example 3 | Transforms can be used to imitate a reference solution. This example checks if a connection in a solution exists in the reference solution, by using the transformreference\_tag that returns all identical legs in a reference solution. |
> |  | %next\_leg\_match\_reference% =   let next\_flight = next(leg(chain), flight\_number),       next\_transit = next(leg(chain), departure) -                      arrival,   any(reference\_tag,       (next(leg(chain), flight\_number) = next\_flight)           and       (next(leg(chain), departure) - arrival = next\_transit)); |
> |  | Start by saving some values from the current leg: the flight number of the next leg and the time length of the connection. After that, look for any matching legs in the reference solution, with the same flight number of the next leg and the same connection time. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.10.html)  | [next](Expressions.05.12.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |