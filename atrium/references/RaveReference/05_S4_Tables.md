## Tables

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.04.html)  | [next](Definitions.06.06.html) |

> Tables
>
> Variables and functions can make choices among values by using the if-then-else operator, which can be nested to any depth. However, if the tests have many outcomes this becomes tedious and inefficient. Tables allow this to be done more elegantly by declaring the tests and then simply list all test cases and the corresponding outcomes. If the test cases are listed in the rule set, the table is an internal table, but it is also possible to define external tables that read the test cases from an external storage the first time the table is accessed.
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Syntax](#22666 "Tables") |
>
> |  |  |
> | --- | --- |
> | • | [Internal tables](#22722 "Tables") |
>
> |  |  |
> | --- | --- |
> | • | [External tables](#22839 "Tables") |
>
> |  |  |
> | --- | --- |
> | • | [External part of external tables](#52773 "Tables") |
>
> |  |  |
> | --- | --- |
> | • | [Special field names](#39961 "Tables") |
>
> |  |  |
> | --- | --- |
> | • | [Aggregation of values in result rows](#23010 "Tables") |
>
> |  |  |
> | --- | --- |
> | • | [Intervals](#23028 "Tables") |
>
> |  |  |
> | --- | --- |
> | • | [Void/null values in external tables](#36022 "Tables") |
>
> Syntax
>
> The syntax for internal and external tables differ, but have some common parts:
>
> |  |  |  |
> | --- | --- | --- |
> | table\_def | ::= | table table\_ident [pformal\_args] =    [alias lets ;]    conditions -> result\_vars ;    tablecont  end |
> | table\_ident | ::= | ident |
> | conditions | ::= | exprs |
>
> Complex tables often use an expression several times. As a convenience, tables may use aliases declared in the beginning of the table. Each alias is an identifier that may be used freely anywhere in the conditions and outcomes but not in the test cases. Note that an alias expression is only evaluated if needed.
>
> The conditions are arbitrary expressions. All conditions are evaluated before trying to find a matching test case. If any condition fails, all defined variables are void.
>
> Which variables that are defined is determined by theresult\_vars.
>
> |  |  |  |
> | --- | --- | --- |
> | result\_vars | ::= | result\_var , result\_vars |result\_var |
>
> Result variables can be exported and given types. The type is optional for internal tables, but mandatory for external tables.
>
> |  |  |  |
> | --- | --- | --- |
> | result\_var | ::= | gexport [durable] [data\_type] var\_ident |
>
> If the table has arguments, allresult\_vars are functions with the same arguments.
>
> Thetablecont part is where the syntax between internal and external tables differ. Internal tables use clusters, whereas external tables contain a reference to the external data source.
>
> |  |  |  |
> | --- | --- | --- |
> | tablecont | ::= | clusters|external [data\_type] extfname ;  patfields -> resfields ;  [edefault]  [remark\_semi] |
>
> Internal tables
>
> Internal tables contain one or more clusters. Each cluster contains one or more rows, where each row contains a list with one test case for each condition and one outcome for each result variable.
>
> |  |  |  |
> | --- | --- | --- |
> | clusters | ::= | clusters & cluster |cluster |
> | cluster | ::= | row \* |
> | row | ::= | test\_cases -> outcomes ; |
>
> The order of the rows does not matter. In order to avoid ambiguity and to catch possible errors, Rave does not allow any two table rows to overlap. This means that the rows of a table must be written in such a way that no condition values can cause two table rows to trigger.
>
> The one exception to this rule is the default row. A row with only wildcard characters for test cases is treated as a default. It is used if none of the other table rows trigger. If none of the rows trigger and there is no default, the table will return void and an error message will be produced.
>
> It is sometimes desirable to construct tables with overlapping test cases where some more specific cases are tried first and then, if none of them match, weaker cases are tried. Clustered tables allow this while avoiding any ambiguity about which row to try first.
>
> When clusters are used the uniqueness rule is relaxed to a certain extent. Rows must still be distinctly non-overlapping within each cluster. The first cluster is tested and if no row triggers, then the next cluster is tried, etc. Only the last cluster may contain a default row.
>
> It is the responsibility of the table author to either include a default for each table, or to make sure that the test cases cover the actual usage of the table.
>
> A test case may just be a constant, matched against its corresponding condition, or be a more complex expression. A test case has the following syntax:
>
> |  |  |  |
> | --- | --- | --- |
> | test\_cases | ::= | test\_cases, test\_case |test\_case |
> | test\_case | ::= | sign\_const |- |y |n |range |
> | range | ::= | anypar sign\_const , sign\_const anypar |relop sign\_const |relop sign\_const or relop sign\_const |relop sign\_const and relop sign\_const |
> | relop | ::= | <> | < | <= | > | >= |
> | anypar | ::= | ( | ) |
>
> The different forms of a test case are explained below:
>
> |  |  |
> | --- | --- |
> | - | A wildcard character: it will match anything. |
> | y n | Synonyms totrue and false that may be used in tables. |
> | (Val1,Val2) )Val1,Val2) (Val1,Val2( )Val1,Val2( | These forms are ranges, fromVal1 to Val2.  An outward pointing parenthesis means that the border value is not included in the range. |
> | <Val <=Val >Val >=Val <>Val | Inequalities that must hold when compared to the condition. |
> | relop Val or relop Val relop Val and relop Val | Combinations of two inequalities from above. Theor case requires either inequality to hold, the and case requires both. |
>
> The outcome of a table is either a dash or an expression. If a dash is used the corresponding result variable will be void.
>
> |  |  |  |
> | --- | --- | --- |
> | outcomes | ::= | outcomes , outcome |outcome |
> | outcome | ::= | expr |
>
> |  |  |
> | --- | --- |
> | Example | table A\_table =      %Flying\_time%, deadhead -> %A\_variable%;     <= 1:00 , y -> 2;     )1:00, 3:00) , y -> 4;     > 3:00 , y -> 6;     <= 1:00 , n -> 3;     )1:00, 3:00) , n -> 5;     > 3:00 , n -> 7; end |
> |  | table A\_reltime\_table(RelTime t)=      arrival\_airport\_city,     %Duty\_time% -> %A\_reltime\_variable%;     "ARN", <= 10:00 -> 12:00;      "ARN", >  10:00 -> 12:00+t;      -,- -> 13:00; end %Another\_variable% = %A\_reltime\_variable%(1:30); |
>
> External tables
>
> External tables are used to facilitate handling of data that is subject to updates.
>
> The test cases and the result values of an external table are loaded into Rave at run-time when the table is accessed for the first time. If the load routine fails, a run-time error will be generated by the system. If the contents of the external table is updated, the rule set should be reloaded to make sure the changes are transferred to the rules.
>
> Aliases are not applicable in external tables, neither are wildcard values and ranges among the test cases. The test cases, which of course are situated in the external part of the table (in the file), must be constants. If the conditions of the table cannot be matched by any of the test cases and there is no default row in the table definition, Rave will generate a run-time error.
>
> The syntax is repeated for thetablecont of an external table.
>
> |  |  |  |
> | --- | --- | --- |
> | tablecont | ::= | external [data\_type] extfname ; |patfields -> resfields ;  [edefault]  [remark\_semi] |
>
> |  |  |
> | --- | --- |
> | Note | Use ofdata\_type after the external keyword is obsolete and is also limited to tables that define one variable only. The recommended method is to write the data\_type before the variable name in resvar. |
>
> External file
>
> The external file name is any string expression. The string can also be a path to a database for those installations that support database access from Rave.
>
> |  |  |  |
> | --- | --- | --- |
> | extfname | ::= | expr |
>
> Table fields
>
> The line after the external declaration contains the name of the fields in the external table. There is onepatfield for each expression and one resfield for each resvar.
>
> |  |  |  |
> | --- | --- | --- |
> | patfields | ::= | patfields , patfield |patfield |
> | resfields | ::= | resfields , resfield |resfield |
>
> The simplest kind of pattern field is the name of a column in the external table. It is also possible to use ranges, see[Intervals](#23028 "Tables").
>
> |  |  |  |
> | --- | --- | --- |
> | patfield | ::= | fieldname |
>
> The preferred way to write afieldname is to use a string, but it is also possible to use an identifier.
>
> |  |  |  |
> | --- | --- | --- |
> | fieldname | ::= | string|ident |
>
> An external table in a database may reference other tables and depending on how Rave accesses the database afieldname may follow references. The following apply for commonly used database back-ends:
>
> |  |  |
> | --- | --- |
> | • | Dave does not support table references. However, Dave implements a UDM reference with a composite foreign key by generating separate fields for each key. These fields are denoted by an underscore (\_) and are addressed individually, for example leg\_key1 and leg\_key2. For more information, see Dave User Guide, Keys and references. |
>
> |  |  |
> | --- | --- |
> | • | Mirador does not support table references, but handles a UDM reference with a composite foreign key directly, as well as through the individual Dave key fields. |
>
> |  |  |
> | --- | --- |
> | • | Mave1 and Mave2 supports table references by using a dot-notation, such as"column.ref-column". They also handle UDM references in the same way as Mirador. In addition, Mave2 supports both (:) and (\_) for addressing individual Dave key fields. |
>
> A result field can be either a field name in the external table or a traverser applied to a field name, see[Aggregation of values in result rows](#23010 "Tables"). It is not legal to mix the two types in the same table.
>
> |  |  |  |
> | --- | --- | --- |
> | resfield | ::= | fieldname opt\_default |traverser\_ident ( fieldname opt\_sep )  opt\_default |
> | opt\_default | ::= | [default expr] |
> | opt\_sep | ::= | [, string\_const] |
>
> The traverser can be used tocount or sum or avg when multiple rows match the same pattern in external tables. The optional separator can only be used with the cat traverser and is limited to a constant string literal. Matching multiple rows is legal for external tables, but not for internal tables.
>
> The default value is used if the field name does not exist in the external table. If no default value is given and the field name is missing, the external table fails and all result variables become void.
>
> Default row
>
> The optional default row in a table consists of the same number of dashes as pattern values and the same number of results as result variables. The values in the default row are used if no earlier alternative matched. Note that the default row has priority over the default value. If both are defined, the value in the default row will be used in case no earlier alternative matched. The default value specified for a missing column is used if there is a matching row, but the column is missing.
>
> |  |  |  |
> | --- | --- | --- |
> | edefault | ::= | dashes -> results ; |
> | dashes | ::= | -|dashes , - |
>
> Remark
>
> To add descriptive text, use the optional remark.
>
> |  |  |  |
> | --- | --- | --- |
> | remark\_semi | ::= | remark ; |
>
> External part of external tables
>
> Rave typically reads a file with a well-defined format when loading an external table. If supported by the main system that uses the rules, access could also be made to other external units, such as tables in a real database managed by a process running on some server machine in the network.
>
> In the Rave default configuration, theTabName (declared in the external table definition in the rule set) refers to a file with the name TabName.etab. This file must be situated in one of a set of directories that the implementation of the system by convention has defined as external table directories. For more information regarding external table management, see the user guide in question. For Crew planning users, see the Crew planning User Guide, External tables. The file is an ASCII file formatted according to this syntax:
>
> NofFields  
> Tfld1,  
> Tfld2,  
> ...,
>
> Val11, Val12, ...;  
> Val21, Val22, ...;  
> ...;
>
> NofFields is an integer specifying the number of fields that the table contains. After this follows the types and names of the fields. The type is defined by a character which may be B, I, R, A, E, or S for Bool, Int, Reltime, Abstime, Enum, and String. The type character is immediately followed by the name of the field. After the field declarations the contents of the table follow. Each value and the field declarations end with a comma. A record can end with either a comma or a semicolon. The semicolon is recommended since it will make it easier to detect errors in the external file. The external file has to end with a new line.
>
> |  |  |
> | --- | --- |
> | Example | 4 Sname, Rduty1, Shomebase, Irank, "ERHA", 123:00, "ARN", 17; "FOBA", 89:00, "ARN", 10; "HEBL", 140:00, "CPH", 42; "TOBO", 112:00, "ARN", 17; "HOHO", 0:00, "CPH", 12; |
> |  | The example shows a table with four fields and five rows. Note that strings are surrounded by double quote characters (") and that each value ends with a comma. White spaces and comments are ignored. The boolean constants true and false may be replaced by y and n. |
>
> The external table file may contain comments on the form:
>
> // A one line comment  
> # Also a one line comment  
> /\* A long, multiline  
>    comment  
> \*/
>
> Some of the fields in an external table file give input to the table definition, some give the results and some may be totally ignored. It is up to the author of the table to decide how the fields should be used.
>
> An external table file can hold all information about the crew. If you are only interested in home base and rank for a given name, write the following definition:
>
> table crew\_table =  
>     %Id% -> String %Homebase%, Int %Rank%;  
>     external "crew\_file";  
>     name -> homebase, rank;  
>     - -> "???", 0;  
> end
>
> This means that, if the type is:
>
> |  |  |
> | --- | --- |
> | • | Bool, the external type must be Bool or Int |
>
> |  |  |
> | --- | --- |
> | • | Int, the external type must be Int |
>
> |  |  |
> | --- | --- |
> | • | Reltime, the external type must be Reltime |
>
> |  |  |
> | --- | --- |
> | • | Abstime, the external type must be Abstime or Int |
>
> |  |  |
> | --- | --- |
> | • | Enum, the external type must be Enum |
>
> |  |  |
> | --- | --- |
> | • | String, the external type must be String. |
>
> The data types of the conditions and the result in the external table declaration in the rule set do not have to coincide exactly with the field declarations in the file, but the types must be compatible.
>
> Special field names
>
> The following special field names exist:
>
> row\_number
>
> A virtual column enumerating all rows.
>
> match\_number
>
> Enumerates all rows that matches the current condition.
>
> row\_number
>
> Rave augments each external table with a virtual column,row\_number. This column contains an enumeration of the data rows of the table. The rows are numbered [1, 2… n], where n is the number of data rows of the table. The type of this column is Int.
>
> |  |  |
> | --- | --- |
> | Note | If the file of an external table already contains a column namedrow\_number, Rave will not generate row numbers for the table. The explicit column in the file overrides the virtual one. |
>
> The Rave programmer uses the row number column as any other column. It can, for example, be used as an index into the table.
>
> |  |  |
> | --- | --- |
> | Example 1 | This table returns the value ofresult\_column in the row with index index\_row in the external table:  table lookup\_example (Int index\_row) =   index\_row -> String %result%;   external "lookup\_example\_file";   row\_number -> result\_column;      -       -> "Row not found"; end |
>
> The row number can also be used as a result column:
>
> |  |  |
> | --- | --- |
> | Example 2 | table output\_example =   %x%  -> Int %row%;   external "output\_example\_file";   xcol -> row\_number; end |
>
> |  |  |
> | --- | --- |
> | Example 3 | Check if a looked up row exists (return a Boolean):  table my\_table =   crew\_id, %flight\_qualification% -> Bool     %crew\_holds\_qualification%;   external "crew\_qual\_file";   CrewId, Qualification -> row\_number;   -, - -> false; end |
>
> |  |  |
> | --- | --- |
> | Note | In database tables,row\_number may only be used in result columns; that is, in the aggregations count(row\_number) and any(row\_number) if row\_number is converted to boolean (to check for row existence). |
>
> match\_number
>
> If a condition matches several rows, the matching rows are enumerated from 1 and up. This enumeration is available in the columnmatch\_number. The match\_number column can only be used as a field name in a patfield. Note that it cannot be used in a range or together with a relational operator.
>
> |  |  |
> | --- | --- |
> | Example 4 | Given the bid file:  2 Ibid, Ibid\_points, 1,1; 2,2; 3,3; 1,10; 2,20; 3,30; 1,100; 2,200; 3,300; |
> |  | the table definition:  table bid\_table(Int bids, Int match) =   bids,match -> int %total\_bid\_points%;   external %bidfile%;   bid,match\_number -> bid\_points; end  gives the following result:  %match1% = %total\_bid\_points%(2,1); equals 2 %match2% = %total\_bid\_points%(2,2); equals 20 %match3% = %total\_bid\_points%(2,3); equals 200 |
>
> Aggregation of values in result rows
>
> An external table will return the first match in the external unit if nothing else is specified. In cases where you are interested in all matching rows, you can use a traverser. Any of the traverserssum, avg, max, min, all, any, count, first, last or cat can be used, or specify the match number in the condition.
>
> In case no row matches, the result is the traverser’s normal value for zero elements (sum of 0 elements is 0, max of 0 elements is void, etc.). It is not allowed to combine result fields with and without traversers and it is neither allowed to have a default row for a table that uses traversers.
>
> |  |  |
> | --- | --- |
> | Example 1 | table sum\_bid\_table =   %bid\_number% -> int %total\_bid\_points%;   external %bidfile%;   bid\_nr -> sum(bid\_points); end |
>
> |  |  |
> | --- | --- |
> | Note | Thecount traverser requires an integer column as argument (like row\_number, which is always available): |
>
> |  |  |
> | --- | --- |
> | Example 2 | table count\_bid\_table =   %bid\_number% -> int %total\_bids%;   external %bidfile%;   bid\_nr -> count(row\_number); end |
>
> Intervals
>
> |  |  |  |
> | --- | --- | --- |
> | patfield | ::= | anypar fieldname , fieldname anypar |relop fieldname |
>
> It is possible to match the value of a condition with an interval in an external table. Suppose that the external table file looks like this:
>
> 5  
> Sdep\_ap,  
> Sarr\_ap,  
> Afrom,  
> Ato,  
> Iresult,  
> "ARN", "CPH", 1Jan1994, 15Jun1994, 1;  
> "ARN", "CPH",16Jun1994, 31Dec1994, 2;  
> "CPH", "FRA", 1Jan1994, 31May1994, 1;  
> "CPH", "FRA", 1Jun1994, 31Oct1994, 2;  
> "CPH", "FRA", 1Nov1994, 31Dec1994, 3;
>
> Each row in the table describes two airports, a date interval and a resulting number. A natural query for the table would be: given a departure airport, an arrival airport and a date and time, what is the value of the result field?
>
> |  |  |
> | --- | --- |
> | Example 1 | This is an example of external Rave table definition that shows how this query can be coded in the Rave language.  %tab\_name% = parameter "exttab"; table interval\_tab =   departure\_airport\_name,   arrival\_airport\_name,   departure -> Int %test\_interval%;   external %tab\_name%;   "dep\_ap", "arr\_ap", ("from","to") -> "result";    -, -, - -> 0; end |
> |  | The ("from","to") part of the table definition refers to two fields in the external file. The third condition of this table must match a record where the value of departure is greater than or equal to the from field and less than or equal to the to field. |
>
> |  |  |
> | --- | --- |
> | Example 2 | table tab1 =    %zot%,departure -> Int %tabval%;   external "etab1";   "fld1", < "fld2" -> "result"; end |
> |  | In this example, a record will match if%zot% = fld1 and departure < fld2. |
> |  | <= FldN (less than or equal to) The relation CondN <= FldN must be true. |
> |  | > FldN (greater than) The relation CondN > FldN must be true. |
> |  | >= FldN (greater than or equal to) The relation CondN >= FldN must be true. |
> |  | <> FldN (not equal to) The relation CondN <> FldN must be true. |
> |  | (FldN, FldN+1)The relations CondN >= FldN and CondN <= FldN+1 must be true. |
> |  | )FldN, FldN+1(The relations CondN > FldN and CondN < FldN+1 must be true. |
> |  | (FldN, FldN+1(The relations CondN >= FldN and CondN < FldN+1 must be true. |
> |  | )FldN, FldN+1)The relations CondN > FldN and CondN <= FldN+1 must be true. |
>
> Void/null values in external tables
>
> Void values can be represented in external tables. In file etables, the stringvoid (without quotation marks) represents a void value, while the string "void" is an ordinary string. In database etables, a value is void if it is NULL in the database.
>
> Records with void values in key columns are only accepted if the values appear in intervals whereas void is accepted within any interval. The lookup key values that are matched against the key columns are never void.
>
> Records with void values in result columns are always accepted. The void value is transferred to the Rave program that uses the etable, and is handled as a normal void value.
>
> Etable traversers over void values work as their corresponding chain traversers:sum, all, any, count and cat never return void. The first and last traversers return void if all matching records are void. The avg, max and min traversers return void if all matching records are void; that is, if there are no non-void records that contribute to the net result.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.04.html)  | [next](Definitions.06.06.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |