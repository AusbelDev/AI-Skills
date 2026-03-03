## Sets

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.06.html)  | [next](Definitions.06.08.html) |

> Sets
>
> Sets provide a simple and convenient way to define categories of things. For instance, to determine whether a certain airport lies within some geographical area, the easiest solution is to define a set containing all the airports within that area.
>
> Sets can be internal or external and the second part of the syntax determines which type of set it is. Internal sets contain a list of constants, whereas external sets contains a reference to the external data source. The syntax for sets is:
>
> |  |  |  |
> | --- | --- | --- |
> | set\_def | ::= | gexport set set\_ident = setcont ; |
> | set\_ident | ::= | ident |
> | setcont | ::= | [parameter] set\_body [remark]  external data\_type setextfname . fieldname [remark] |
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Internal sets](#52439 "Sets") |
>
> |  |  |
> | --- | --- |
> | • | [External sets](#23188 "Sets") |
>
> |  |  |
> | --- | --- |
> | • | [Using sets](#23223 "Sets") |
>
> Internal sets
>
> |  |  |  |
> | --- | --- | --- |
> | set\_body | ::= | set\_body , sign\_const |sign\_const |
>
> All members of a set are constants and must have the same data type.
>
> |  |  |
> | --- | --- |
> | Example | set asian\_airports = "BKK","SIN","HKG","PEK","NRT"; |
>
> The contents of parameterized internal sets can be updated from the run-time system. An element may be removed or added without having to recompile and reload the rule set.
>
> |  |  |
> | --- | --- |
> | Note | Internal sets must have at least one member in the source code. If the set is a parameter then the user can make the set empty. |
>
> External sets
>
> Repeat the syntax for thesetcont of an external table.
>
> |  |  |  |
> | --- | --- | --- |
> | setcont | ::= | external data\_type setextfname . fieldname [remark] |
> | setextfname | ::= | ( expr ) |qual\_var\_ident [pexprs] |keyword [pexprs] |string |
>
> External sets get their members from external storage, for example a file. The layout of the external storage is exactly the same as the layout of external tables. The field name is the name of the field that will be used to collect the members of the set. If the external file contains more than one field, only the field specified in the external set definition is used. The other fields are ignored. The file may contain duplicates. Several tables and rule sets may simultaneously refer to the same external file and just use different combinations of the fields.
>
> |  |  |
> | --- | --- |
> | Example | Two examples of external set definitions:  set african\_airports  =    external string "aairport"."ap";  set american\_airports =   external string %tabname%."ap"; |
> |  | In this example the fieldap in the external file aairport is used to define the members of the set african\_airports; and the field ap in the file as given in the variable %tabname%, defines the members of the set american\_airports. |
>
> Using sets
>
> A set is used through thein operator. For example, the expression   
> %arrival\_airport\_name% in african\_airports   
> checks if a flight arrives at an airport in Africa, provided that the set african\_airports has been properly defined.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.06.html)  | [next](Definitions.06.08.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |