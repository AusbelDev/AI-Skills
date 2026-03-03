## Abstime

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.5.html)  | [next](Data_Types.04.7.html) |

> Abstime
>
> An absolute time represents the time and date of an event. Absolute times have a resolution of 1 minute. The guaranteed legal value range is from 1 January 1901 up to and including 31 December 2099, but only legal dates are allowed (a date such as Feb 31 raises an error).
>
> If a time is given, it must be in the interval0:00 to 24:00 inclusive. Minutes must be in the interval 0 to 59. This is different from reltime, where minutes can be any integer.
>
> The year can be either in the range1901-2100, or 0-99. In the latter, case numbers above 85 are interpreted as 1900 plus the given year, and 85 and below are interpreted as 2000 plus the given year.
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | data\_type | ::= | abstime |
> | abstime\_const | ::= | month day year reltime\_const |month\_day year reltime\_const |day month year [ reltime\_const ] |day month\_year [ reltime\_const ] |
> | month | ::= | jan | feb | mar | apr | may | jun | jul | aug | sep | oct | nov | dec |
> | month\_day | ::= | a month followed by a day without intervening space. |
> | month\_year | ::= | a month followed by a year without intervening space. |
> | day | ::= | int\_const |
> | year | ::= | int\_const |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.5.html)  | [next](Data_Types.04.7.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |