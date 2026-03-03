## Range

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.13.html)  | [next](Definitions.06.01.html) |

> Range
>
> If the dependency of an expression can be seen as the object for which the calculation is done, the range of an expression is the lowest level that includes all objects that may affect the expression. In other words, the range indicates how much of a chain a calculation uses.
>
> |  |  |
> | --- | --- |
> | Example | In this expression, both dependency and range isleg.  %block\_time% = arrival - departure;  In this expression, the dependency isleg, while the range is duty. Whenever the duty changes, the expression must be reevaluated.  %leg\_cxn\_time% = next(leg(duty), departure) - arrival; |
>
> When performance is vital, for example when Rave is used for optimization, it is recommended to model the problem so that expressions and rules get as narrow ranges as possible. A leg rule with a range that includes the whole chain will decrease performance. Such a rule will be rechecked on each leg in the chain, even if only a small part of the chain has been modified, because the optimizer checks rules and modifies chains iteratively.
>
> |  |  |
> | --- | --- |
> | See also | [Dependencies and objects](Expressions.05.02.html#40273 "Dependencies and objects") [Improving the performance of Rave code](App_Modelling_Info.10.2.html#22026 "Improving the performance of Rave code") |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.13.html)  | [next](Definitions.06.01.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |