## Contexts

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.10.html)  | [next](Definitions.06.12.html) |

> Contexts
>
> The iterator construction is used to divide data into subsets. The result may be some chains, some legs or some rotations. The context construction is used to refer to the original data, for example all chains in the window and all rotations.
>
> Contexts are defined in a similar way as keywords. The configuration is therefore application-dependent.
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Using a context](#23774 "Contexts") |
>
> |  |  |
> | --- | --- |
> | • | [Default context](#23810 "Contexts") |
>
> |  |  |
> | --- | --- |
> | • | [Current context](#23827 "Contexts") |
>
> Using a context
>
> The syntax for a context is:
>
> |  |  |  |
> | --- | --- | --- |
> | prim\_expr | ::= | context ( context , expr ) |
> | context | ::= | ident|default\_context |current\_context |
>
> All contexts available with the context construction are also available as report language loops.
>
> |  |  |
> | --- | --- |
> | Example 1 | context(sp\_crrs, count(chain\_set)) |
>
> Iterators used inside the context construction are applied on all objects associated with that context. The expression in the example counts all chains in the sub-plan.
>
> In the same way as with iterators, the objects in a context are represented with one, randomly chosen, object. Therefore, expressions that do not aggregate over all objects in the context have no well-defined meaning.
>
> |  |  |
> | --- | --- |
> | Example 2 | context(sp\_crrs,flight\_number)  In this expression, the flight number will be collected from any leg in the sub-plan. |
>
> Default context
>
> The default context is a special construction that is used if no context is explicitly stated.
>
> |  |  |
> | --- | --- |
> | Example 1 | count(chain\_set) |
>
> If the expression is not used inside a context construction, the default context will be used.
>
> |  |  |
> | --- | --- |
> | Example 2 | context(default\_context, count(chain\_set)) |
>
> If used from the top level, this expression is identical to the previous expression. The only difference is that the default context is explicitly stated.
>
> If used inside another iterator expression, the expression will always return all chains in the default context for example, all chains in the window.
>
> Current context
>
> The current context is a special construction that is used to refer to all chains in the context that originally was used. The context is similar to the default context, but the result may vary depending on where the context is used.
>
> |  |  |
> | --- | --- |
> | Example 1 | context(default\_context,     sum(chain\_set,           context(current\_context, ...  The current context will return all objects in the default context. |
>
> |  |  |
> | --- | --- |
> | Example 2 | context(sp\_crrs,     sum(chain\_set,        context(current\_context, ...  The current context will return all objects in thesp\_crrs context. |
>
> The current context may be used to write definitions that will be usable regardless of what context they are used in.
>
> |  |  |
> | --- | --- |
> | Example 3 | %all\_chains% = context(current\_context, count(chain\_set)); (100 \* count(chain\_set) where(%something%)) / %all\_chains%  This example describes how to calculate the percentage of the chains that fulfils%something%. The definition %all\_chains% will calculate the total number of chains in the active context. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.10.html)  | [next](Definitions.06.12.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |