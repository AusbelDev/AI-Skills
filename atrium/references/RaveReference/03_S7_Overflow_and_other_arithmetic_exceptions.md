## Overflow and other arithmetic exceptions

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.7.html)  | [next](Data_Types.04.9.html) |

> Overflow and other arithmetic exceptions
>
> Integer, reltime and abstime types are stored with a limited precision and the guaranteed ranges described in previous sections. If very large integers or times are manipulated, an overflow can occur. Rave does not detect or repair overflow conditions. A division by zero will result in a run-time error and the outcome of a rule legality check is undefined in such a case.
>
> |  |  |
> | --- | --- |
> | Note | It is the responsibility of the Rave programmer to avoid overflow and division-by-zero situations. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.7.html)  | [next](Data_Types.04.9.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |