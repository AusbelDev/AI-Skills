## Iterators

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.09.html)  | [next](Definitions.06.11.html) |

> Iterators
>
> Sometimes it is not enough to calculate values for objects in one chain. The iterator construction allows calculations, for example, on all chains in the active plan, on all the rotations or on all selected crew members. Iterators must be defined by a Rave programmer.
>
> An iterator partitions the active set of objects. It starts with a data set (for example, all trips in the active plan or the result from another iterator) and divides it into subsets.
>
> Even though iterators are defined by a Rave programmer, there are also some special built-in iterators. See[Built-in iterators](Expressions.05.10.html#22698 "Iterators and contexts").
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Defining an iterator](#23510 "Iterators") |
>
> |  |  |
> | --- | --- |
> | • | [Using the iterator](#44838 "Iterators") |
>
> |  |  |
> | --- | --- |
> | • | [Mixing iterators and levels in traversers](#23720 "Iterators") |
>
> |  |  |
> | --- | --- |
> | • | [Iterator aliases](#23750 "Iterators") |
>
> Defining an iterator
>
> An iterator definition always operates on sets, where the members are defined as, or constructed from, level objects. In addition to defining new iterators it is possible to create alias names for existing iterators.
>
> |  |  |  |
> | --- | --- | --- |
> | iter\_def | ::= | gexport iterator iter\_ident =     partition ( qual\_ident ) [bykeys]    [remark\_semi]  end  |gexport iterator iter\_ident =    qual\_iterator\_ident ; |
> | iter\_ident | ::= | ident |
>
> If the optionalbykeys part is omitted, each set has exactly one member.
>
> |  |  |
> | --- | --- |
> | Example 1 | iterator leg\_set =   partition(leg); end |
> |  | iterator chain\_set =   partition(chain); end |
>
> Thebykeys can be used to collect objects for which all keys are identical in the same set.
>
> |  |  |  |
> | --- | --- | --- |
> | bykeys | ::= | by ( keys ) |
> | keys | ::= | key|key , keys |
> | key | ::= | expr |
>
> The following example makes sets of all legs arriving at the same airport and all legs with the same flight number.
>
> |  |  |
> | --- | --- |
> | Example 2 | iterator arrival\_airports =   partition(leg)     by(arrival\_airport\_name); end |
> |  | iterator flight\_number\_set =   partition(leg)     by(flight\_number); end |
>
> Multiple keys can be used to collect, for example, all legs with the same departure airport, flight number and deadhead.
>
> |  |  |
> | --- | --- |
> | Example 3 | iterator flight =   partition(leg)   by(departure\_airport\_name,     flight\_number, deadhead); end |
>
> By comparing attributes not only for one object, but for a sequence of objects, it is possible to define attribute matches for many objects. This is done with themap construction.
>
> |  |  |  |
> | --- | --- | --- |
> | key | ::= | map ( travkey , keys ) |
>
> |  |  |
> | --- | --- |
> | Example 4 | iterator compressed\_chain =   partition(chain)   by(map(leg(chain),departure\_airport\_name,                    flight\_number, deadhead); end  This iterator puts all chains that have the same structure and for which each leg has the same value for the three attributes, in the same group. |
> |  | Consider the following case: |
> |  | All attributes in the first two chains are identical and will be put in the same subset. The last chain will be put in a separate subset (the attribute departure airport is different between the two subsets). |
>
> |  |  |
> | --- | --- |
> | Note | If one of the keys in an iterator definition evaluates tovoid, the object is skipped; that is, it is not considered in the partition. |
>
> Using the iterator
>
> Iterators may be used in traversers and in report language loops. Since the objects divided by iterators do not necessarily have a well-defined order, thewhile construction should not be used together with iterators.
>
> When iterators are used in a traverser, the traverser will be applied on each group created by the iterator.
>
> |  |  |
> | --- | --- |
> | Example 1 | count(compressed\_chain)  Counts the number of unique chains. |
>
> |  |  |
> | --- | --- |
> | Example 2 | max(compressed\_chain, count(leg\_set))  For each subset created by the iteratorcompressed\_chain, every leg in every chain is counted. The result of the total expression will be the maximum number of legs in a compressed chain. |
>
> As demonstrated, an expression in traversers with iterators can contain another iterator expression. But it may also contain an ordinary expression that uses the active subset, or any object in the active subset.
>
> |  |  |
> | --- | --- |
> | Example 3 | max(flight\_number\_set,flight\_number)  This expression will result in the maximal flight number. The flight number attribute is collected from any leg object in the active group. But since all legs in one group are guaranteed to have the same flight number, this does not matter. |
>
> |  |  |
> | --- | --- |
> | Example 4 | max(arrival\_airports,flight\_number)  /\* BAD \*/  In this expression, the flight number will be collected from any leg in each arrival airport group. |
>
> |  |  |
> | --- | --- |
> | Note | In the last example only thearrival\_airport attribute is guaranteed to be identical for all legs in the group. It is the responsibility of the Rave programmers to only use expressions that are well-defined together with an iterator. |
>
> Mixing iterators and levels in traversers
>
> As mentioned in the previous section, it is of vital importance that an expression used inside an iterator traverser makes sense. A common mistake is to mix traversers using iterators and traversers using levels in a way that makes the calculation arbitrary.
>
> |  |  |
> | --- | --- |
> | Example 1 | Assume that you are interested in finding out the maximum numbers of legs arriving to an airport.  max(arrival\_airports, count(leg(chain))  /\* BAD \*/ |
> |  | For each active arrival airport group, thecount traverser will be applied. But since the count aggregate is using a level instead of an iterator, the expression will be applied on an arbitrary chain. Even if the active arrival airport group contains legs from 5 chains, only one chain will be used in the count traverser. Also, all legs in that chain will be counted, not only those arriving at the active airport. |
> |  | max(arrival\_airports, count(leg\_set))  If the level traverser is replaced with an iterator traverser, each leg arriving at a specific airport will be counted. |
>
> Sometimes it can make sense to replace the iterator with an ordinary level traverser.
>
> |  |  |
> | --- | --- |
> | Example 2 | sum(chain\_set, sum(leg(chain), departure-arrival))  This expression will calculate the total block time for all chains. Thesum(leg(chain) traverser will always be applied on only one chain because it is used inside the built-in chain\_set iterator. Therefore it is perfectly all right to use a standard level traverser instead of an iterator traverser. |
>
> Iterator aliases
>
> An iterator alias can be used to refer to the same iterator using different names.
>
> |  |  |
> | --- | --- |
> | Example | iterator roster\_set = chain\_set; |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.09.html)  | [next](Definitions.06.11.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |