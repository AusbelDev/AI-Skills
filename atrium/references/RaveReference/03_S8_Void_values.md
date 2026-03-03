## Void values

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.8.html)  | [next](Expressions.05.01.html) |

> Void values
>
> Expressions in the Rave language do not always have a well-defined value. For instance, thenext and prev traversers could refer to an object that does not exist (because the current object is the last or the first object). When Rave runs into something like this, it ignores the rest of the expression and returns void.
>
> A void return value is transferred, according to certain rules, from a primary expression to more complex ones. It is important to realize that a rule that is evaluated to void in a certain context will not be tested in that context, this means the rule is regarded as legal.
>
> An expression returning void always starts with an expression that does not have a well-defined value in a certain context. Here is how this void value is transferred through more complex expressions:
>
> |  |  |
> | --- | --- |
> | • | All unary and binary expressions with a void operand are void. |
>
> |  |  |
> | --- | --- |
> | • | The traversersfirst, last, next and prev return void if the expression is void, or if the traverser refers to an object that does not exist. |
>
> |  |  |
> | --- | --- |
> | • | The traversersavg, max and min do not return void if there is at least one object that contributes to the net result with a non-void value. On the other hand, if all contributions are void or if there are no objects that apply (because of a filter or a where condition), these traversers return void. |
>
> |  |  |
> | --- | --- |
> | • | A traverser returns void if it specifies a from- or to-point that does not exist. |
>
> |  |  |
> | --- | --- |
> | • | Unless they have a non-existing from- or to-point, the traverserssum, count, all, any and cat never return void. If no objects apply or if all contributions are void, sum and count return zero (0), all returns true, any returns false, and cat returns the empty string (""). |
>
> |  |  |
> | --- | --- |
> | • | Built-in and user defined functions return void if any of the arguments are void. The only exceptions are the functionsvoid and default. |
>
> |  |  |
> | --- | --- |
> | • | If then else returns void if the condition is void or if the applicable expression is void. The two first examples below return void. The last one is not void. If <void> then <not void> else <not void>; If <true> then <void> else <not void>; If <false> then <void> else <not void>; |
>
> |  |  |
> | --- | --- |
> | • | Context or transform return void if the result of the context or the transform is an empty set of objects. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.8.html)  | [next](Expressions.05.01.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |