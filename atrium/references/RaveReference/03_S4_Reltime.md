## Reltime

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.4.html)  | [next](Data_Types.04.6.html) |

> Reltime
>
> A relative time represents a period of time between two events, or a time of day. Relative times have a resolution of 1 minute and the guaranteed range is approximately +/- 4,000 years.
>
> Both the hour and the minutes must be legal integers and the value after converting a reltime to minutes must also fit in an integer.
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | data\_type | ::= | reltime |
> | reltime\_const | ::= | hour : minute |
> | hour | ::= | int\_const |
> | minute | ::= | int\_const |
>
> |  |  |
> | --- | --- |
> | Note | There are no limits on the minutes or hours. For example, 40:100 is a valid reltime and is interpreted as 41 hours and 40 minutes. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.4.html)  | [next](Data_Types.04.6.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |