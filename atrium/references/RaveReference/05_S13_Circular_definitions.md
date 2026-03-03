## Circular definitions

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.13.html)  | [next](Modules.07.1.html) |

> Circular definitions
>
> Recursive definitions are not supported in the language and it is not possible to do circular definitions of any kind. The compiler analyzes the rule set and generates an error message if a circular definition is found.
>
> |  |  |
> | --- | --- |
> | Example | Example of an illegal circular definition:  %X% =   if is\_first(leg(chain))        then 0:00       else %Y%;%Y% = %X% + arrival - departure; |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.13.html)  | [next](Modules.07.1.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |