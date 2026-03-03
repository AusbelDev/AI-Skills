## Enum

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.6.html)  | [next](Data_Types.04.8.html) |

> Enum
>
> Rave supports user-defined enumeration types, which can be used whenever a variable has a limited number of legal values. By using an enumeration type you can limit the values of a parameter to only the legal choices.
>
> |  |  |
> | --- | --- |
> | Example | enum targets =   max\_roster;   production; end  %target% = parameter production remark "Target for optimizer"; %cost% =   if %target%=production then %production\_cost%   else %max\_roster\_cost%; |
> |  | The code above restricts the planner to select betweenmax\_roster or production. If targets was a string, the planner could easily misspell the input and if targets was an integer the planner would need to know the encoding. For example, does 0 represent max\_roster or production? |
>
> The Rave compiler checks that enumeration types are used in a type-correct way. This is very useful for tables. If enums are used instead of strings to encode a limited set of alternatives, the compiler can check that there are no illegal values caused by misspelling in the Rave code. This also works for values in external tables, although the check is performed when the table is accessed the first time instead of at compilation. All values in the external table are verified when the table is first accessed and the run-time system will notify the user of any illegal value. If strings are used, an error may remain for a long time: until circumstances occur that can make the Rave code need the misspelt value.
>
> The reserved wordenum defines an enumeration type and all legal values in that type. Each enum type and all its values must be unique in its scope. If an enum type is exported all its values are also exported. The same is true for global export. Enum values of the same type can be compared with each other. The first enum value in a type is the smallest.
>
> Theenum type and each value can have its own remark.
>
> Neither enum types nor enum values can be redefined via inheritance in child modules. Only enum remarks can be redefined.
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | enum\_def | ::= | gexport enum enum\_ident =   enum\_values   [ remark ; ] end |
> | enum\_ident | ::= | ident |
> | enum\_values | ::= | enum\_values enum\_value |enum\_value |
> | enum\_value | ::= | ident remark; |
> | data\_type | ::= | qual\_enum\_ident |
> | enum\_const | ::= | qual\_enum\_value |
>
> For explanations ofgexport and the qual-prefix, see [Modules](Modules.07.1.html#21842 "Modules").

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Data_Types.04.6.html)  | [next](Data_Types.04.8.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |