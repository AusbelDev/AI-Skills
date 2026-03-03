## Matrices

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.05.html)  | [next](Definitions.06.07.html) |

> Matrices
>
> A matrix provides a compact alternative to a table with two conditions. It is plainer and handier than a two-dimensional table.
>
> The syntax for matrices is:
>
> |  |  |  |
> | --- | --- | --- |
> | matrix\_def | ::= | matrix matrix\_ident [ pformal\_args ] =    [alias lets ;]    condition , condition -> result\_var;    test\_cases ;    matrix\_row+  end |
> | matrix\_ident | ::= | ident |
> | condition | ::= | expr |
> | matrix\_row | ::= | test\_case; matrix\_outcomes ; |
> | matrix\_outcomes | ::= | matrix\_outcomes, matrix\_outcome |matrix\_outcome |
> | matrix\_outcome | ::= | expr|- |
>
> The conditions (always two), test cases and outcomes have the same general form as in tables.
>
> The test cases and outcomes are expressed in a matrix of columns and rows. The first row contains the test cases for the first condition. The first column contains the test cases for the second condition. The other values are the outcomes.
>
> The outcome may be specified as void (for examplevoid\_int). If the outcome is a wildcard character (-), the interpretation is that the matrix does not provide a value for such a case. A void value is returned and an error message is produced.
>
> The uniqueness rules in tables also apply to matrices.
>
> |  |  |
> | --- | --- |
> | Example | matrix max\_flight\_duty\_time\_base =  %nr\_of\_landings%,         %duty\_check\_in\_time% -> export ax\_flight\_duty\_time\_base%;                          0, (1,2), 3, 4, >=5;         (05:30,05:59); 00:00, 10:30, 10:00, 09:30, 08:45;         (06:00,06:29); 00:00, 11:00, 10:30, 10:00, 09:15;         (06:30,06:59); 00:00, 11:30, 11:00, 10:30, 09:45;         (07:00,18:29); 00:00, 12:00, 11:30, 11:00, 10:15;         (18:30,04:29); 00:00, 09:00, 08:30, 08:00, 07:15;         (04:30,04:59); 00:00, 09:30, 09:00, 08:30, 07:45;         (05:00,05:29); 00:00, 10:00, 09:30, 09:00, 08:15; end  If%nr\_of\_landings% is 3 and %duty\_check\_in\_time% is 06.15, then the value assigned to %max\_flight\_duty\_time\_base% is 10.30. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.05.html)  | [next](Definitions.06.07.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |