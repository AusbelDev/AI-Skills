## Data types and constants

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Syntax.09.11.html)  | [next](App_Syntax.09.13.html) |

> Data types and constants
>
> The lexical class of constants includes six different data types: integers, booleans, strings, relative times, absolute times, and enums.
>
> This section covers the following data types:
>
> |  |  |
> | --- | --- |
> | • | [Int](#22220 "Data types and constants") |
>
> |  |  |
> | --- | --- |
> | • | [Bool](#22224 "Data types and constants") |
>
> |  |  |
> | --- | --- |
> | • | [String](#22229 "Data types and constants") |
>
> |  |  |
> | --- | --- |
> | • | [Reltime](#22234 "Data types and constants") |
>
> |  |  |
> | --- | --- |
> | • | [Abstime](#22238 "Data types and constants") |
>
> |  |  |
> | --- | --- |
> | • | [Enum](#22242 "Data types and constants") |
>
> The syntax for the name and format of each data type are:
>
> |  |  |  |
> | --- | --- | --- |
> | data\_type | ::= | int | bool | string | reltime | abstime |qual\_enum\_ident |
> | const | ::= | int\_const | bool\_const | string\_const |reltime\_const | abstime\_const |qual\_enum\_value |
> | int\_const | ::= | one or more digits,0-9 |
> | bool\_const | ::= | true | false |
> | string\_const | ::= | string+ |
> | string | ::= | A sequence of characters enclosed in". All characters can be used except:  " \ newline  The following escape combinations can be used:  \" \\ \n (newline) \t (tab) |
> | reltime\_const | ::= | hour : minute |
> | hour | ::= | int\_const |
> | minute | ::= | int\_const |
> | abstime\_const | ::= | month day year reltime\_const |month\_day year reltime\_const |day month year [ reltime\_const ] |day month\_year [ reltime\_const ] |
> | month | ::= | jan | feb | mar | apr | may | jun |jul | aug | sep | oct | nov | dec |
> | month\_day | ::= | A month followed by a day without intervening space. |
> | month\_year | ::= | A month followed by a year without intervening space. |
> | day | ::= | int\_const |
> | enum\_def | ::= | gexport enum enum\_ident =   enum\_values   [ remark ; ] end |
> | enum\_ident | ::= | ident |
> | enum\_values | ::= | enum\_values enum\_value |enum\_value |
> | enum\_value | ::= | ident remark ; |
> | qual\_enum\_value | ::= | [module . ] enum\_value |
> | qual\_enum\_ident | ::= | [module . ] enum\_ident |
> | year | ::= | int\_const |
>
> Int
>
> Integer constants consist of a (non-empty) sequence of digits.
>
> Bool
>
> A boolean constant is one of the reserved wordstrue or false.
>
> String
>
> A string constant is a (possibly empty) sequence of characters enclosed in double quotes. There is no explicit limit to the length of a string.
>
> A string in Rave can contain any printable character in the ISO-8859-1 (Latin-1) or UTF-8 character set.
>
> Reltime
>
> A relative time constant consists of an integer constant followed by a colon and another integer constant. The relative time constant expresses hours and minutes.
>
> Abstime
>
> An absolute time constant expresses a fixed point in time.
>
> |  |  |
> | --- | --- |
> | Note | When using Rave with Crew & Ops Management solutions the maximum limit of Abstime is 31dec2036. |
>
> Enum
>
> The reserved wordenum defines an enumeration type and all legal values in that type. Each enum type and all its values must be unique in its scope. If an enum type is exported, then all its values are also exported. The same is true for global export. Enum values of the same type can be compared with each other. The first enum value in a type is the smallest.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Syntax.09.11.html)  | [next](App_Syntax.09.13.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |