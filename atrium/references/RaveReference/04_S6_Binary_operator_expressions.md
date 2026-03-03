## Binary operator expressions

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.06.html)  | [next](Expressions.05.08.html) |

> Binary operator expressions
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | expr multiplicative expr |expr additive expr |expr relational expr |expr logical expr |expr membership qual\_ident |
>
> The binary expressions are divided into a few different classes:
>
> |  |  |
> | --- | --- |
> | • | [Multiplicative](#34633 "Binary operator expressions") |
>
> |  |  |
> | --- | --- |
> | • | [Additive](#22194 "Binary operator expressions") |
>
> |  |  |
> | --- | --- |
> | • | [Relational](#22278 "Binary operator expressions") |
>
> |  |  |
> | --- | --- |
> | • | [Logical](#22323 "Binary operator expressions") |
>
> |  |  |
> | --- | --- |
> | • | [Set membership](#22358 "Binary operator expressions") |
>
> Multiplicative
>
> |  |  |  |
> | --- | --- | --- |
> | multiplicative | ::= | \* |/ |mod |
>
> where
>
> |  |  |
> | --- | --- |
> | \* | gives integer multiplication. |
> | / | gives integer division, for example8/5 = 1.  The result is negative if one operand is negative and the other positive. |
> | mod | gives the remainder of the division,  for example8 mod 5 = 3.  The result is negative if the left operand is negative. |
>
> Combinations of data types give the following results.
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | Left operand | Operator | Right operand | Result |
> | integer | \* | integer | integer |
> | integer | \* | reltime | reltime |
> | reltime | \* | integer | reltime |
> | integer | / | integer | integer |
> | reltime | / | integer | reltime |
> | reltime | / | reltime | integer |
> | integer | mod | integer | integer |
> | reltime | mod | reltime | reltime |
>
> Additive
>
> |  |  |  |
> | --- | --- | --- |
> | additive | ::= | + |- |
>
> Combinations of data types give the following results.
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | Left operand | Operator | Right operand | Result |
> | integer | + | integer | integer |
> | reltime | + | reltime | reltime |
> | abstime | + | reltime | abstime |
> | reltime | + | abstime | abstime |
> | integer | - | integer | integer |
> | reltime | - | reltime | reltime |
> | abstime | - | abstime | reltime |
> | abstime | - | reltime | abstime |
>
> Relational
>
> |  |  |  |
> | --- | --- | --- |
> | relational | ::= | =|<> |< |<= |> |>= |
>
> wheretrue is returned if the operands fulfil the corresponding condition:
>
> |  |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- |
> | = | equal | < | less than | <= | less than or equal |
> | <> | not equal | > | greater than | >= | greater than or equal |
>
> The relational operators compare two values and return a boolean;true if the comparison holds, false if not. Relations can be applied to operands of any data type, but both operands must have the same type.
>
> Integers are compared by numerical value (-2 < 17). Reltimes and abstimes are compared similarly. false is less than true.
>
> Strings are compared alphabetically character by character according to the ASCII table. This implies among others that digits are less than uppercase letters, which in turn are less than lowercase letters. The ordering of national characters is undefined due to the used character set.
>
> Logical
>
> |  |  |  |
> | --- | --- | --- |
> | logical | ::= | and |and2 |or |or2 |
>
> where
>
> |  |  |
> | --- | --- |
> | and, and2 | returnstrue if both operands are true. |
> | or, or2 | returnstrue if either operand is true. |
>
> The logical operators require boolean operands and give boolean results.
>
> The difference betweenand/or and and2/or2 is that and/or evaluates the second argument only if necessary, while and2/or2 always evaluates both arguments. Therefore, if either argument becomes void, the expression using and2/or2 becomes void, but the expression using and/or might not be if the first operand is not void.
>
> A consequence of this is that (x and2 y) is identical to (y and2 x) but (x and y) is not the same as (y and x).
>
> Set membership
>
> |  |  |  |
> | --- | --- | --- |
> | membership | ::= | [not] in |
>
> where
>
> |  |  |
> | --- | --- |
> | in | returnstrue if the left operand is a member of the right operand. |
>
> The right operand must be an identifier that has been declared as a set. The data type of the left operand must match the type of the members in the set.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.06.html)  | [next](Expressions.05.08.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |