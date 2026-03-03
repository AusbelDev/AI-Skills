## Primary expressions

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.04.html)  | [next](Expressions.05.06.html) |

> Primary expressions
>
> A primary expression is either one of the basic elements: variable, keyword, function, constant or a parenthesized expression. Parenthesized expressions can be used to control the evaluation order of an expression, or simply to make the code more readable.
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | qual\_var\_ident [pexprs] |keyword [pexprs] |function [pexprs] |const |( expr ) |
> | pexprs | ::= | ( exprs ) |
> | exprs | ::= | exprs , expr |expr |
> | const | ::= | bool\_const|abstime\_const |reltime\_const |int\_const |string\_const |enum\_const |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.04.html)  | [next](Expressions.05.06.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |