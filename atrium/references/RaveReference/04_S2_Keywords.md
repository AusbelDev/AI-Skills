## Keywords

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.02.html)  | [next](Expressions.05.04.html) |

> Keywords
>
> Keywords are used to access information about an object, for example a flight, and should be seen as the basic attributes of the objects. By combining keywords you can create more advanced expressions, rules and costs.
>
> All keywords are system-configurable and which keywords that are available depend on which application the rules should be used in. Each keyword has a specific data type and a dependency level and some also take additional arguments. A keyword has the dependency level constant, atomic, or full chain and constitutes an attribute for all objects on that level.
>
> |  |  |
> | --- | --- |
> | Example | Adding attributes to the level hierarchy.  Given that you havearrival and departure as predefined leg keywords, you can create two new attributes:  /\* Block time is the time between departure and arrival \*/ %block\_time% = arrival - departure;  /\* Aggregated block time for a duty. \*/ /\* Take the sum of %block\_time% for each leg in the duty \*/ %duty\_block\_time% = sum(leg(duty), %block\_time%); |
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | keyword [pexprs] |
> | keyword | ::= | ident |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.02.html)  | [next](Expressions.05.04.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |