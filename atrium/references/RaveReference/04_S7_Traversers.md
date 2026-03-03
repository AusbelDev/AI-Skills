## Traversers

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.07.html)  | [next](Expressions.05.09.html) |

> Traversers
>
> Traversers allow an expression to be evaluated within one or more objects of the same level (see[Levels](Definitions.06.09.html#23316 "Levels")), with each value contributing to the net result.
>
> |  |  |
> | --- | --- |
> | • | [Syntax](#22411 "Traversers") |
>
> |  |  |
> | --- | --- |
> | • | [Description](#22425 "Traversers") |
>
> |  |  |
> | --- | --- |
> | • | [From, to, while and where](#39491 "Traversers") |
>
> |  |  |
> | --- | --- |
> | • | [Void values](#37945 "Traversers") |
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | expr | ::= | trav\_ident (trav\_key, expr) [trav\_spec] |trav\_ident (trav\_key [trav\_spec], expr ) |trav\_ident0 (trav\_key) [trav\_spec] |trav\_ident0 (trav\_key [trav\_spec]) |trav\_cat |
> | trav\_ident | ::= | sum | avg |max | min |all | any |first | last |next | prev |earliest | latest |
> | trav\_cat | ::= | cat (trav\_key, ident, ident [sep])  [trav\_spec] |cat (trav\_key [trav\_spec], ident, ident,  [sep]) |
> | sep | ::= | string |
> | trav\_ident0 | ::= | count|is\_first | is\_last |
> | trav\_key | ::= | qual\_level\_ident ( expr ) |
>
> Description
>
> A traverser operates on objects of the type stated in thequal\_level\_ident within a larger "parent" level defined by the expression part of the trav\_key. This is best illustrated by an example:
>
> |  |  |
> | --- | --- |
> | Example 1 | sum(leg(trip),arrival-departure) |
>
> In example 1, the traverser operates on all leg objects within a certain trip object (trip is a "larger", "higher", or "parent" level in the example). The result is the sum of all the flight times within one trip object.
>
> The traversers are:
>
> sum, avg
>
> The data type of the expression can beinteger or reltime and the traverser result is integer or reltime respectively.
>
> sum returns the sum of all expressions , avg returns the sum divided by the number of expressions.
>
> If no cases apply (for instance if thewhere condition is always false) the sum-traverser returns 0 and the avg-traverser returns void.
>
> max, min
>
> The expression can be of any type and the traverser result is of the same type.max returns the largest and min the smallest value.
>
> If no cases apply (for instance if thewhere condition is always false), both the min- and the max-traverser return void.
>
> all, any
>
> The expression must be boolean and the result is boolean.all returns true if all values are true and any returns true if any value is true.
>
> Both traversers return as soon as possible. For instance, ifall finds one value that is false it returns false immediately, without computing the remaining values. If no cases apply, for instance if the where condition is always false, the all-traverser returns true and the any-traverser returns false.
>
> count
>
> Unlike most other traversers,count takes only one argument, namely the level. count returns the number of iterations. count(level(plevel)) is identical to sum(level(plevel),1).
>
> cat
>
> The expression must be string and the result is a concatenation of those strings. The concatenated string is built from the first to the last matching object, no matter if the traversal is done forwards or backwards.
>
> If no cases apply, for instance if thewhere condition is always false, the cat-traverser returns the empty string.
>
> Note that heavy usage of string functions can have a negative impact on the performance of the system. Also note that the concatenated string will be truncated if the result is longer than 4095 characters.
>
> Thecat traverser may be equipped with an additional separator argument.
>
> |  |  |
> | --- | --- |
> | Example 2 | cat(leg(duty), departure\_airport\_name, ", ")  Here,",  " is a separator argument for the string concatenation and a possible result of the traverser is "AMS, LHR, GOT, BRU". |
>
> first, last
>
> The expression may be of any type. It is evaluated in the context of the first or the last level object within the parent level.
>
> |  |  |
> | --- | --- |
> | Example 3 | last(leg(duty),arrival) - first(leg(duty),departure)  This expression computes the working time counted from the first departure to the last arrival of one duty object. |
>
> earliest, latest
>
> Synonyms forfirst and last.
>
> next, prev
>
> The expression may be of any type. It is evaluated for the next level object within the parent level. If no such object exists the result is void.
>
> |  |  |
> | --- | --- |
> | Example 4 | departure - prev(leg(rtd),arrival)  This expression computes the ground time prior to a certain leg object. |
>
> is\_first, is\_last
>
> Likecount these only have a level argument. They return true if the current level is the first or last within the parent level.
>
> From, to, while and where
>
> Traversers can be combined with an optional specification on how to traverse. The specification can be to start from a specific point and to traverse to another specified point, or to traverse while a certain condition istrue.
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | trav\_spec | ::= | from [towhile] [where] |towhile [where] |where [while] |
> | towhile | ::= | to |while |
> | where | ::= | where ( expr ) |
> | from | ::= | from ( trav\_point [where] ) |from ( current ) |
> | to | ::= | to ( trav\_point [where] ) |to ( current ) |
> | while | ::= | [direction] while ( expr ) |
> | direction | ::= | forwards |backwards |
> | trav\_point | ::= | first |last |next |prev |
>
> Description
>
> Whenfrom and to are used together, the from point always has to precede the to point in the chain. Combinations where the order of the points cannot be determined during compilation are not allowed. Accepted combinations are:
>
> |  |  |
> | --- | --- |
> | from | to |
> | first | anything |
> | anything | last |
> | prev [ where ( expr ) ] | prev |
> | prev [ where ( expr ) ] | current |
> | current | current |
> | current | next [ where ( expr ) ] |
> | next | next [ where ( expr ) ] |
> | prev [ where ( expr ) ] | next [ where ( expr ) ] |
>
> Omittingfrom and/or to is the same as specifying from(first) and to(last) respectively.
>
> |  |  |
> | --- | --- |
> | Example 1 | from(first where(cond)) to (current)  This expression is not allowed, as thefrom point might occur after current. |
>
> Thewhile construction is used for traversing while the specified condition is true. When the condition is evaluated as false, the traverser terminates. The direction is important when using the while condition and it can be specified as forwards or backwards. If the direction part is omitted, the default is forwards. If no from point is given, the default starting point is first, but if only a backwards while condition is specified, the default starting point is last.
>
> If awhere condition is included, only those expressions for which the where condition is true are taken to the traverser. The others are simply skipped. For optimal performance, you should replace parts of a where condition with a from, to and/or while condition whenever possible
>
> Awhile condition is always evaluated before a where condition (or a filter, which can be regarded as a shorthand for where; see [Filters](Definitions.06.08.html#23226 "Filters")).
>
> |  |  |
> | --- | --- |
> | Example 2 | next(leg(rtd),departure) where(not deadhead) - arrival)  computes the time between the active leg and the departure of the next leg that is not a deadhead flight. |
> |  | is\_last(leg(rtd)) where(deadhead)  istrue if the active leg is the last leg in the active duty that is a deadhead. |
> |  | let this\_departure=departure;  sum(leg(crr), %block\_time%) from(current) forwards         while(departure<this\_departure + 8:00);  sums up the block time in a time window of 8 hours. |
>
> Aprev or next traverser can have a while condition if it also has a where condition. This can improve performance in cases where the prev or next traversal can be aborted using the while statement.
>
> |  |  |
> | --- | --- |
> | Note | Thewhile condition is mainly used for performance reasons, in order to terminate the traverser and avoid unnecessary evaluations. while is always evaluated before evaluating a where condition (or a filter). |
>
> Void values
>
> The handling of void values is described in[Void values](Data_Types.04.9.html#22072 "Void values").

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.07.html)  | [next](Expressions.05.09.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |