## Constraints

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.03.html)  | [next](Definitions.06.05.html) |

> Constraints
>
> Constraints are a special type of rules designed to take advantage of the built-in constraint checking capabilities of different optimizers, and at the same time provide the same legality check for applications without these capabilities. Any differences between applications are handled by the constraint construct.
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Syntax](#22508 "Constraints") |
>
> |  |  |
> | --- | --- |
> | • | [Condition](#22516 "Constraints") |
>
> |  |  |
> | --- | --- |
> | • | [Foreach](#22555 "Constraints") |
>
> |  |  |
> | --- | --- |
> | • | [Nonadditive](#44509 "Constraints") |
>
> |  |  |
> | --- | --- |
> | • | [Cost](#22614 "Constraints") |
>
> |  |  |
> | --- | --- |
> | • | [Constraint failtext](#40779 "Constraints") |
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | constraint\_def | ::= | gexport constraint [ponoff] constr\_name =   [valid ;]   (foreach ;)\*   constr\_condition ;   [nonadditive(formal\_args) = expr ;]   [cost [(expr)] = expr ;]   [failtext ;]   [remark ;]   [group\_def] end |
> | ponoff | ::= | ( (on | off) ) |
> | constr\_name | ::= | ident |
>
> The reserved wordconstraint identifies a new constraint with the name constr\_name. In the same way as with rules, the status of a constraint can be changed during a session and the optional ponoff sets the initial status. To check if a constraint is enabled, use the built-in rule\_on() function. See [Rule functions](Expressions.05.13.html#23201 "Built-in functions"). After the equal sign (=) the constraint body defines the constraint. The end of the body is marked with the word end. The body parts valid and failtext have the same meaning as for rules.
>
> If a constraint is level-dependent, only the left-hand side of the constraint condition is allowed to depend on anything outside this level. This applies also to chain constants (for example thehomebase keyword in a crew pairing problem).
>
> A group within a constraint can contain any Rave definition, not just the ones that can be used for regular groups (see[Groups](Definitions.06.12.html#23863 "Groups")). Groups in constraints are used as hints to the optimizers. For more information, see the optimizer documentation.
>
> Condition
>
> The only mandatory part of the constraint body is theconstr\_condition. It is limited to the traversers shown below:
>
> |  |  |  |
> | --- | --- | --- |
> | constr\_condition | ::= | sum(c\_set, expr) [where (expr)] c\_op c\_rhs |count(c\_set) [where (expr)] c\_op c\_rhs |
> | c\_op | ::= | <= | >= | = |
> | c\_rhs | ::= | expr |
> | c\_set | ::= | context | transform\_ident |
>
> Thesum and count are followed by a relational operator, c\_op and a right- hand-side expression, c\_rhs. The traversers can optionally be limited with a where clause.
>
> The data to be traversed, specified by thec\_set, must be an application-defined context or transform.
>
> |  |  |
> | --- | --- |
> | Example | constraint max\_inexperienced =   valid leg.%is\_flight\_duty%;   count(equal\_legs) where (crew.%is\_inexperienced%) <= 1; end  This constraint limits the number of inexperienced crew members on a flight to a maximum of one. |
>
> The termglobal constraint is often used when the data in a constraint is specified by a context, and the term vertical constraint is used when the data is specified by a transform.
>
> Some application-defined transforms, for exampleequal\_trips, refer to a user-defined level with an application-defined name. This name must be connected to the real name of the user-defined level by a level alias defined in the \_topmodule (or as a global export in any other module), for example:
>
> level trip\_defined\_in\_ruleset = level.trip;
>
> Foreach
>
> Theforeach part of a constraint provides a convenient way to define a number of similar constraints that only differ in a single value.
>
> |  |  |
> | --- | --- |
> | Example | This constraint defines a constraint for each day of a planning period.  constraint head\_constraint\_crew =   foreach day in set(1, %days\_in\_planning\_period%);   sum(sp\_crew\_chains, %trip\_unass%(day)) <= %max\_heads%;   failtext %head\_failtext%(day,false); end |
>
> The value range of the different constraints is defined by theforeach\_set set, which can be a set name, an enum name, or a range. The example above has a range (interval) from 1 to the number of days in the planning period.
>
> The loop variable (day in the example) is associated with the current day number and can be used by other expressions in the constraint.
>
> The general syntax of theforeach part is:
>
> |  |  |  |
> | --- | --- | --- |
> | foreach | ::= | foreach lvar in foreach\_set [alias(expr)] [ispec] |
> | lvar | ::= | ident |
> | foreach\_set | ::= | set\_ident | enum\_ident | range\_set |
> | ispec | ::= | where (expr) [while (expr)] |while (expr) [where (expr)] |
> | set\_ident | ::= | ident |
> | enum\_ident | ::= | ident |
> | range\_set | ::= | set (start, end [, step]) |
>
> Values in the set can be filtered with awhere and/or a while specification. Both of these may access the loop variable.
>
> It is possible to specify more than oneforeach part, creating a multi-dimensional matrix of constraints. Each loop variable must be unique within the constraint and an expression of a foreach part may refer to loop variables defined in preceding foreach parts.
>
> Thealias defines a presentation value for each constraint in the set. This value may, for instance, include a loop variable to create a unique string for each constraint. The scope and dependency of the expression must have the same restrictions as the constraint, but the expression has no impact on the Rave code.
>
> |  |  |
> | --- | --- |
> | Note | The expressions in aforeach part may not return void. |
>
> More about ranges
>
> The set of values used in constraintforeach variables can be defined by a range in the following ways:
>
> |  |  |
> | --- | --- |
> | • | foreach n in set(start, end); |
>
> |  |  |
> | --- | --- |
> | • | foreach n in set(start, end, step); |
>
> The element type is either Enum, Int, Reltime, or Abstime.start, end, and step must be of the same type, except in Abstime sets, where step is a Reltime. The optional step argument makes it possible to skip values within a range. If step is excluded, it defaults to 1 (for Int sets) or 0:01 (Abstimes or Reltimes). A step value of 0 is considered an error, and the constraint will not be evaluated. The step argument is not allowed for Enum types.
>
> The resulting set consists of the set of valuesstart+n\*step that are in the range [start, end], or in the range [end, start] if step is negative. The set becomes empty if:
>
> |  |  |
> | --- | --- |
> | • | start > end and step > 0, or |
>
> |  |  |
> | --- | --- |
> | • | start < end and step < 0. |
>
> |  |  |
> | --- | --- |
> | Example 1 | set(1,5) = set(1,5,1) = 1,2,3,4,5 set(1,5,3) = 1,4 set(3,0,-1) = 3,2,1,0 set(3,0) = set(3,0,1) = <empty range> set(1,5,-1) = <empty range> |
>
> |  |  |
> | --- | --- |
> | Example 2 | Note that Abstime ranges can become very large if no step is specified:  set(1Jan2009 0:00, 2Jan2009 0:00) = set(1Jan2009 0:00, 2Jan2009 0:00, 0:01) = 1Jan2009 0:00, 1Jan2009 0:01, 1Jan2009 0:02, 1Jan2009 0:03, ... |
>
> Nonadditive
>
> Thenonadditive function is an advanced feature that provides more information about the constraint expression to optimizers, helping them improve their performance. It does not change the behaviour of the constraint in any way.
>
> The feature defines a local function, which can be used in the constraint condition.
>
> |  |  |
> | --- | --- |
> | Example | constraint muc\_4\_day\_trips =  sum(sp\_crrs, nonadditive(homebase, %trip\_nr\_of\_days%)) <= 2;  nonadditive(String base, Int days) =   if base = "MUC" and days = 4 then 1 else 0;  cost = 10000; end |
>
> |  |  |
> | --- | --- |
> | See also | Crew Pairing Optimizer Reference, Nonadditive constraints |
>
> Cost
>
> If the condition of a constraint is false, the constraint is violated and the tested solution is illegal. However, you can define a constraint that allows violations and adds a cost to the solution instead. There are two types of violation costs:
>
> |  |  |
> | --- | --- |
> | • | cost =expr\_lin\_cost; |
>
> |  |  |
> | --- | --- |
> | • | cost (when max expr\_max\_violation) = expr\_bin\_cost; |
>
> The first type defines a linear cost, and the second a binary cost. The violation of a constraint is calculated as the absolute value of the difference between the left-hand and right-hand side of the condition. If reltime values are compared, the violation is the difference in number of minutes. The legality and cost of a constraint depend on the violation and the type of cost.
>
> A constraint is only legal if at least one of the following criteria is true:
>
> |  |  |
> | --- | --- |
> | • | violation is 0 |
>
> |  |  |
> | --- | --- |
> | • | it has a linear cost,expr\_lin\_cost |
>
> |  |  |
> | --- | --- |
> | • | it has a binary cost,expr\_bin\_cost, and the violation is less than or equal to the limit, expr\_max\_violation |
>
> Depending on the type of cost, the cost of a constraint is:
>
> |  |  |
> | --- | --- |
> | no cost | always 0 |
> | linear cost | expr\_lin\_cost \* violation |
> | binary cost | expr\_bin\_cost if the violation is less than or equal to the limit, expr\_max\_violation, 0 otherwise. |
>
> The expressions in a cost definition,expr\_lin\_cost, expr\_bin\_cost, and expr\_max\_violation, have to return integers and cannot return void. Not all applications support all cost types, and some applications may require a cost definition. Please refer to the documentation of each application for details.
>
> |  |  |
> | --- | --- |
> | Example 1 | The following constraint has a linear cost. For each required but missing Japanese-speaking crew member on a flight leg, the constraint adds the cost given by the parameter%GLC\_jap\_speaker\_cost\_parameter%.  constraint (on) jap\_speaker\_constraint =   valid language.%jap\_speakers\_required% > 0;   sum(equal\_legs, %num\_jap\_speakers%) >=                 language.%jap\_speakers\_required%;   cost = %GLC\_jap\_speaker\_cost\_parameter%;   remark "(GLC) Global constraint to ensure sufficient nr of Japanese speakers"; end |
>
> |  |  |  |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | Example 2 | The following rules apply for the number of inexperienced crew members on a flight leg:  |  |  | | --- | --- | | • | 0 or 1 inexperienced crew member is legal |  |  |  | | --- | --- | | • | 2 or 3 inexperienced crew members is legal, but at a cost |  |  |  | | --- | --- | | • | more than 3 inexperienced crew members is illegal |  The corresponding constraint uses a binary cost,%max\_inexp\_cost%.  constraint (on) max\_total\_inexperienced\_crew\_constraint:   count(equal\_legs) where (%crew\_is\_inexperienced%) <=             %max\_inexp\_with\_no\_cost%;   cost(when max %max\_inxep\_violation%) = %max\_inexp\_cost% end  %max\_inexp\_with\_no\_cost% = 1; %max\_inxep\_violation% = 2; %max\_inexp\_cost% =   parameter 1000; |
>
> Optimizers automatically include costs of violated constraints when minimizing the total cost of a solution, therefore it is not necessary to add costs of constraints to a common cost definition.
>
> Constraint failtext
>
> This is an example of a constraint that uses afailtext message. The lhs and rhs arguments are integers in order to match the type of the left and right side of the constraint condition.
>
> |  |  |
> | --- | --- |
> | Example | constraint four\_day\_trips\_per\_base =   foreach base in active\_bases;     sum(sp\_crrs, nonadditive(homebase, %caldays%)) <=             %long\_trip\_limit%(base);     nonadditive(String a\_base, Int caldays) =                if a\_base = base and caldays = 4 then 1 else 0;   cost = 10000;   failtext(Int lhs, Int rhs) =         concat(format\_int(lhs, "%i"), " long trips on base ",               base, ", exceeds ", format\_int(rhs, "%i")); end |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.03.html)  | [next](Definitions.06.05.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |