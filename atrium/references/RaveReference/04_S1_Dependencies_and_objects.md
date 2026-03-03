## Dependencies and objects

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.01.html)  | [next](Expressions.05.03.html) |

> Dependencies and objects
>
> The fundamental data model of Rave is a chain of objects (for example a trip containing a number of legs). Any number of additional levels, such as duty, can be added by the Rave programmer. See[Levels](Definitions.06.09.html#23316 "Levels") for more details of how levels are defined and named.
>
> |  |  |
> | --- | --- |
> | Example | A level structure with leg, duty and trip levels. |
>
> The level structure in the example is used for all examples in this manual. Trip is the full chain representing a schedule where a crew member starts and ends at the same base. Duty corresponds to a day of work and a leg is the smallest planning unit, a single flight from one airport to another.
>
> All expressions in the language operate on the available level objects. In fact, an expression always belongs to and defines an attribute for a certain level. A flight’s departure and arrival times are attributes on the leg level and the sum of block times within a duty will be a duty attribute. The level an expression defines an attribute to is called the dependency of the expression.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.01.html)  | [next](Expressions.05.03.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |