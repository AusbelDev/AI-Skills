## Variables and functions

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.01.html)  | [next](Definitions.06.03.html) |

> Variables and functions
>
> A variable or function allows a Rave programmer to define the necessary steps to compute a desired value. Complex rule sets are usually built by writing variables and functions in a layered manner, where complex definitions are expressed in terms of simpler ones.
>
> The top level variables are ultimately used inside rules for legality checking. They are also used in reports defined by the report writer or to provide information for other parts of the system (for instance serving as system parameters).
>
> A definition can take on one of three basic forms: an expression, a parameter or a table value. See also[Tables](Definitions.06.05.html#22635 "Tables").
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Expression](#21923 "Variables and functions") |
>
> |  |  |
> | --- | --- |
> | • | [Data type](#21973 "Variables and functions") |
>
> |  |  |
> | --- | --- |
> | • | [Parameters](#21988 "Variables and functions") |
>
> |  |  |
> | --- | --- |
> | • | [Local variables](#22026 "Variables and functions") |
>
> |  |  |
> | --- | --- |
> | • | [Remark](#22073 "Variables and functions") |
>
> Expression
>
> The most general form of variable definition has the following syntax:
>
> |  |  |  |
> | --- | --- | --- |
> | var\_def | ::= | gexport [durable] var\_ident [pformal\_args]=   [ local\_var ]   var\_body   [remark ] ; |
> | var\_ident | ::= | %one or more characters, % is not legal % |
> | var\_body | ::= | expr |
>
> If there are any arguments, this is called a function definition, otherwise it is called a variable definition.
>
> |  |  |
> | --- | --- |
> | Note | All arguments must be explicitly typed and if any argument is void the function will return void. |
>
> Thevar\_ident is the name of the defined variable or function.
>
> |  |  |  |
> | --- | --- | --- |
> | pformal\_args | ::= | ( formal\_args ) |
> | formal\_args | ::= | formal\_args , formal\_arg |formal\_arg |
> | formal\_arg | ::= | data\_type ident |
>
> A variable/function can contain locally named expressions, see[Local variables](#22026 "Variables and functions").
>
> |  |  |
> | --- | --- |
> | See also | [Durable caches for variables](App_Modelling_Info.10.2.html#37081 "Improving the performance of Rave code") |
>
> Data type
>
> Each variable or function has a data type. The type follows from the expression defining the variable and is automatically inferred by Rave with no need for any manual help.
>
> The expression must be internally consistent for Rave to accept the definition and each expression containing the variable is also checked for consistency. Each detected mismatch results in an error message from Rave.
>
> |  |  |
> | --- | --- |
> | Example | /\* Int Variable \*/ %number\_of\_deadheads% = count(leg(trip)) where (deadhead);  /\* Bool Variable \*/ %connection\_ok% = %connection\_time% > 1:00;  /\* String Variable \*/ %nightstop\_station% = last(leg(duty), arrival\_airport\_name); |
> |  | /\* Reltime Variable \*/ %block\_time% = arrival - departure;  /\* Abstime Variable \*/ %duty\_end% = last(leg(duty), arrival) + 1:00;  /\* String Function, with String argument \*/ %operates\_on%(String day) =      locate(day, days\_of\_operation) > 0; |
>
> Parameters
>
> Parameters allow certain values in a rule set to be tuned from a menu while the system is running, without having to recompile the rule set. Parameter settings can be stored together with plans, hereby providing an individualized rule set.
>
> The syntax of a parameter is:
>
> |  |  |  |
> | --- | --- | --- |
> | par\_def | ::= | gexport [durable] var\_ident =   par\_body   [remark] ; |
> | par\_body | ::= | parameter par\_const [par\_limit] |
>
> Parameters can be limited; they can have a minimum and/or a maximum allowed value.
>
> |  |  |  |
> | --- | --- | --- |
> | par\_limit | ::= | minvalue par\_const |maxvalue par\_const |minvalue par\_const maxvalue par\_const |maxvalue par\_const minvalue par\_const |
> | par\_const | ::= | sign\_const |
>
> The constantpar\_const, supplied in par\_body, is the default value used when the rule set is first loaded and can later be overridden by changing the parameter from a menu. The constants in par\_limit are the minimum and maximum values for the parameter. They are used by the run-time system to check the range of the new values that are given to the parameter.
>
> |  |  |
> | --- | --- |
> | Example | %briefing% = parameter 1:00 minvalue 0:50 maxvalue 2:00; |
>
> Local variables
>
> The general form of variable/function definitions may optionally contain local variables.
>
> The syntax for defining local variables is:
>
> |  |  |  |
> | --- | --- | --- |
> | local\_var | ::= | let lets ; |
> | lets | ::= | lets , let |let |
> | let | ::= | ident = expr |
>
> Each identifier in thelet rule introduces a new local variable. The value of the new variable is given by the expression. The local variables defined may be used inside the main definition, but are not available anywhere else. Also, an earlier local variable can be used in the definition of a later local variable.
>
> Local variables are evaluated immediately. If any of the local variables has a void value, the whole definition becomes void, regardless of if and how these local variables are used.
>
> The local variables are computed in the order they are given. Whenever a local variable occurs inside an expression its value is substituted as if it were a constant. Note that local variables are not merely a convenient short-hand notation, they also provide functionality not otherwise available.
>
> |  |  |
> | --- | --- |
> | Example | %work\_time\_24h% =     let start = %duty\_start%,         stop = start + 24:00;     sum(duty(trip),         overlap(%duty\_start%,%duty\_end%,start,stop))         from(current) while(%duty\_start%<=stop); |
> |  | %duty\_start% =     first(leg(duty),departure) - %briefing%; %duty\_end% =     last(leg(duty),arrival) + %debriefing%; %briefing% =     parameter 0:45; %debriefing% =     parameter 0:30 |
> |  | This example uses local variables in a way that is very common. The variables%work\_time\_24h%, %duty\_start% and %duty\_end% have duty dependency, they will be calculated for each duty. Every time %work\_time\_24h% is calculated, the following happens:  |  |  | | --- | --- | | • | The local variablestart gets the value of %duty\_start% for the current duty. |  |  |  | | --- | --- | | • | The local variablestop gets the same value + 24:00. | |
> |  | |  |  | | --- | --- | | • | The traversersum(duty(trip),...) calculates the sum of the results from the function call (%duty\_start%,...), which is called for all duty objects in the trip that touches the 24h period. It traverses from the current duty and forwards while it finds more duties in the time window. Every time the overlap function is called, the variables %duty\_start% and %duty\_end% get new values, whereas the local variables, start and stop, are constant throughout the whole traverser. | |
> |  | |  |  | | --- | --- | | • | The result of the traverser is also the result of the variable%work\_time\_24h%. |  The value of%work\_time\_24h% could not have been calculated without the existence of local variables. |
>
> Remark
>
> Definitions such as a parameters and rules can be equipped with a remark string. The remark is used for presentation to the planner or end user. It can be used when presenting the result of a legality check, or in a parameter form.
>
> The remark can be composed of several sections, for example a brief description, usually the name of the parameter/rule in plain language and another more detailed section for the planner. The available roles for the documentation are configurable.
>
> The syntax for remarks is:
>
> |  |  |  |
> | --- | --- | --- |
> | remark | ::= | remark role\_remarks |
> | role\_remarks | ::= | role\_remark , role\_remarks |role\_remark |
> | role\_remark | ::= | [role] [+] string |
> | role | ::= | ident |
>
> The+ in role\_remark can be used to extend a comment when redefining a variable, see [Modules](Modules.07.1.html#21842 "Modules").
>
> |  |  |
> | --- | --- |
> | Example | %max\_duties\_in\_trip% = parameter 2   remark "Maximum number of Duties in a Trip",   planner "Controls trip length according to GTP18 paragraph"; |
>
> By using\n and \t, it is possible to include line breaks and indents in a remark. See also [String](Data_Types.04.4.html#24932 "String").

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.01.html)  | [next](Definitions.06.03.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |