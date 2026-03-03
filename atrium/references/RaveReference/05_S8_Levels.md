## Levels

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.08.html)  | [next](Definitions.06.10.html) |

> Levels
>
> The level construction is used to define objects to be available in the rules and how these objects are related to each other.
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Syntax](#23368 "Levels") |
>
> |  |  |
> | --- | --- |
> | • | [Atomic level](#23371 "Levels") |
>
> |  |  |
> | --- | --- |
> | • | [Full chain level](#23380 "Levels") |
>
> |  |  |
> | --- | --- |
> | • | [General level](#23391 "Levels") |
>
> |  |  |
> | --- | --- |
> | • | [Constraints when defining levels](#23433 "Levels") |
>
> |  |  |
> | --- | --- |
> | • | [Writing levels with good performance](#23444 "Levels") |
>
> |  |  |
> | --- | --- |
> | • | [Parallel level hierarchies](#23447 "Levels") |
>
> |  |  |
> | --- | --- |
> | • | [Level aliases](#23479 "Levels") |
>
> There is always one atomic level and one level describing the full chain. Between these levels an arbitrary number of levels can be introduced. Each level, except the atomic level and the full chain level, is defined in terms of an already defined level. The first level, for example duty, will be defined in terms of the atomic level. The second level, for example trip, will be defined in terms of the previous level and so on. It is also possible to define parallel levels, for example a number of levels defined in terms of the leg level.
>
> In addition to defining new levels, it is possible to create alias names for existing levels.
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | level\_def | ::= | gexport level level\_ident =   level\_body   [remark ;]  end |gexport level level\_ident = qual\_ident ; |
> | level\_ident | ::= | ident |
> | level\_body | ::= | when( bool\_const ); |(is\_first | is\_last) (qual\_ident) when (expr); |
>
> Atomic level
>
> The definition of the atomic object is needed to name the smallest available object. This atom level is used in at least one other level definition.
>
> |  |  |
> | --- | --- |
> | Example | level leg =    when(true); end |
>
> Full chain level
>
> The definition of the full chain object is needed to name the object containing the full chain. The chain level is also needed to refer to other objects, when defining the general levels, see[General level](#23391 "Levels").
>
> |  |  |
> | --- | --- |
> | Example | The full chain level is used in most level definitions.  level trip =    when(false); end |
>
> General level
>
> All level definitions, except the ones for the atomic and the full chain levels, use already defined levels. That is, a new level is based on an already existing level. The definition describes when an object of the already defined level is the last or the first object in the new level object.
>
> |  |  |
> | --- | --- |
> | Example 1 | The following definition could be read like this: A leg is the last leg in a duty when the connection time between two legs is greater than 8 hours.  level duty =    is\_last(leg)   when(next(leg(trip),departure)-arrival >= 8:00 ); end |
> |  |  |
>
> |  |  |
> | --- | --- |
> | Example 2 | The following definition is equivalent to the previous one. The difference is that the first object is defined instead of the last.  level duty =    is\_first(leg)   when(departure - prev(leg(trip), arrival) >= 8:00); end |
>
> Constraints when defining levels
>
> The expression defining a specific level may not refer, directly or indirectly, to levels that are defined using the particular level itself.
>
> |  |  |
> | --- | --- |
> | Example | level duty=    is\_last(leg)   when(is\_last(leg(duty)); end  This level definition is not valid, as the expression defining the level uses the level itself. |
>
> It is not allowed to use iterators in level definitions.
>
> Writing levels with good performance
>
> Complicated levels are a source for bad system performance. General tips for good performance is to use simple level expressions and to stick to the most important levels (leg, duty and trip for crew pairing and additional levels wop, roster and maybe month for crew rostering).
>
> Parallel level hierarchies
>
> Levels are defined in a hierarchy. The atomic level is the base of the hierarchy. Other levels are based on the atomic level or on other levels in the hierarchy. It is possible to define many levels based on the same existing level.
>
> |  |  |
> | --- | --- |
> | Example | level duty =   is\_last(leg)   when(%new\_working\_day%); end |
> |  | level month=   is\_last(leg)   when(%new\_month%); end |
> |  | The levels duty and month are both based on the leg level. |
>
> Level aliases
>
> A level alias can be used to refer to the same level using different names.
>
> |  |  |
> | --- | --- |
> | Example | level roster = chain; |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.08.html)  | [next](Definitions.06.10.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |