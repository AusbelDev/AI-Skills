## Rules

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.02.html)  | [next](Definitions.06.04.html) |

> Rules
>
> Rules are the main tools for legality checking. When a legality check is ordered from an application, all rules are tried. Depending on how a rule is defined, the chain of objects it is tried on, and the number of objects of each level, a single rule may be applied several times or not at all, as appropriate under the circumstances.
>
> This repetition is handled automatically by Rave and does not need intervention from the Rave programmer.
>
> Legality checks can originate from several places. During automatic planning a large number of checks is done on partial solutions and guides the search and optimization process. During manual planning, the system runs legality checks automatically in the background to inform the user as soon as possible when rules are violated.
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Syntax](#63202 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Repetition](#22180 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Turning rules on or off](#22197 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Validity statements](#22206 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Rule exceptions](#48082 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Rule hierarchies](#22256 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Penalties and quality rules](#22315 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Rule violation cost](#71284 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Messages (failtext)](#22435 "Rules") |
>
> |  |  |
> | --- | --- |
> | • | [Rule failures](#61352 "Rules") |
>
> Syntax
>
> |  |  |  |
> | --- | --- | --- |
> | rule\_def | ::= | gexport rule [ponoff] rule\_name =   [valid ;]   (exception ;)\*   rule\_condition ;   [delta ;]   [cost = expr;]   [max\_penalty ;]   [min\_penalty ;]   [failtext ;]   [failobject ;]   [severity ;]   [deadline ;]   [overshoot\_min\_limit ;]   [overshoot\_max\_limit ;]   [remark ;] end |
> | rule\_name | ::= | ident |
> | rule\_condition | ::= | expr inequality expr |
>
> |  |  |
> | --- | --- |
> | Note | The statements in a rule definition can occur in any order. |
>
> Therule\_name is the name of the rule. The rule\_condition is any boolean expression and it is the only mandatory part of the rule body.
>
> |  |  |
> | --- | --- |
> | Example | rule not\_too\_many\_landings =      %number\_of\_landings% <= 5;  end |
>
> You should write your rules in such a manner that they are not violated because of incomplete trips. For instance, if a certain rotation with a total of 10 legs is legal, then the first 5 legs should also be legal. The reason for this is that complete rotations are built up, during both manual and automatic planning. During manual planning, incompleteness would cause many unfounded complaints by the system. During automatic planning it would disrupt the optimization.
>
> If therule\_condition evaluates to void the rule is regarded as legal.
>
> Repetition
>
> Similar to expressions, a rule has a dependency: it belongs to a certain level. A rule will be evaluated and tested for all objects at this level. The dependency of a rule is automatically calculated by Rave by looking at the expressions that are part of the rule.
>
> |  |  |
> | --- | --- |
> | Example | rule connection\_ok =      next(leg(duty),departure) - arrival > 1:00; end  This rule will be repeated for all leg objects, since the expression of the rule has this dependency. |
>
> Turning rules on or off
>
> |  |  |  |
> | --- | --- | --- |
> | ponoff | ::= | ( (on | off) ) |
>
> Individual rules may be enabled or disabled from a menu during a planning session, without recompiling or even reloading the rule set. A disabled rule is ignored during legality checking. When a rule set is loaded, all rules are by default enabled. Rules may optionally contain a status part indicating whether the rule should initially be enabled (on) or disabled (off).
>
> |  |  |
> | --- | --- |
> | Example | rule (off) A\_rule =      %Number\_of\_landings% <= 5; end |
>
> To check if a rule is enabled, use the built-inrule\_on() function. See [Rule functions](Expressions.05.13.html#23201 "Built-in functions").
>
> Validity statements
>
> A rule may carry a validity statement that restricts its applicability.
>
> The syntax is:
>
> |  |  |  |
> | --- | --- | --- |
> | valid | ::= | [valid expr ;] |
>
> If the expression of the valid section of the rule is void orfalse, the rule is ignored.
>
> |  |  |
> | --- | --- |
> | Example | rule not\_too\_many\_landings =     VALID %shorthaul%;      %number\_of\_landings% <= 5; end  The rule in the example will only be checked if the value of the expression%shorthaul% is true. |
>
> When combining validity statement and rule condition, the rule in the example above is evaluated according to the following table:
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | %number\_of\_landings% <= 5 | %shorthaul% true | %shorthaul% false | %shorthaul% void |
> | true | legal | ignored | ignored |
> | false | illegal | ignored | ignored |
> | void | legal | ignored | ignored |
>
> Rule exceptions
>
> Rule exceptions are used to relax or completely ignore a rule for a particular time period and crew.
>
> The interval where a violated rule should be excepted is modelled by defining the rule’s start and/or end time; see example. Both dates are specified as abstimes.
>
> |  |  |  |
> | --- | --- | --- |
> | exception | ::= | startdate = expr ; |enddate = expr ; |startday = expr ; |endday = expr ; |
>
> |  |  |
> | --- | --- |
> | Example | Example of a generated external table for rule exceptions, where crew 37642 is allowed to have 3 extra wop duty days for the wop that starts 10Feb2005:  SCrewId, SRuleId, ASdate, IOverInt, ROverRel, "37642", "max\_wop\_duty\_days", 10Feb2005, 3, 0:00, ... |
> |  | startdate needs to be defined for rules that use rule exceptions. The generated data from the rule exception table is used in its expression.  rule max\_wop\_duty\_days =     startdate = wop.%start%;     wop.%days% <=          %max\_wop\_days% +          %exception\_overshoot\_int%(wop.%start%); end |
> |  | table rule\_exceptions(Abstime SDate) =     crr\_crew\_id, current\_rule\_id, SDate ->         Bool %rule\_turned\_off%,         Int %exception\_overshoot\_int%,         Reltime %exception\_overshoot\_rel%;     external "SpLocal/RuleExceptions";     CrewId, RuleId, Sdate -> turnoff, OverInt, OverRel;     -,-,- -> false, 0, 0:00; end |
>
> For some more modelling tips, see[Rule exception mechanism](App_Modelling_Info.10.4.html#22367 "Rule exception mechanism").
>
> Rule hierarchies
>
> Rules may also be grouped into a hierarchy, indicating that they belong together. The grouping is accomplished by parent rules that have no actual contents of their own; they just refer to other rule(s).
>
> The parent rule syntax is:
>
> |  |  |  |
> | --- | --- | --- |
> | parent\_rule\_def | ::= | gexport rule [ponoff] rule\_name =   [valid ;]   [module .] rule\_name is legal ;   [remark ;] end |
> | module | ::= | ident |
>
> A parent rule may contain a status part indicating whether it is enabled. When a parent rule is disabled, all its sub-rules are automatically disabled. This is a help to enable/disable many rules at once. It is however also possible to explicitly enable a sub-rule, even though its parent rule is disabled. A parent rule may also have a validity statement and if this is the case, this will be inherited by all its sub-rules.
>
> |  |  |
> | --- | --- |
> | Example 1 | rule Main\_rule =      Sub\_rule\_1 is legal;      Sub\_rule\_2 is legal;  end |
> |  | rule Sub\_rule\_1 =      %X% = 7;  end |
> |  | rule Sub\_rule\_2 =      %Y% >5;  end |
>
> A rule may have multiple parent rules. This allows rules to be grouped into partially overlapping sets. If all of the parents are disabled, the rule will also be turned off. A rule inherits the validity statements from all its parents. The disjunction of these statements must betrue for the rule to be applied, that is if any of the parent rules are valid, the sub-rule will also be valid.
>
> |  |  |
> | --- | --- |
> | Example 2 | rule FD\_longhaul =     VALID %FD% AND %Longhaul%;     FD\_long\_r1 is legal;     FD\_r1 is legal; end |
> |  | rule FD\_shorthaul =     VALID %FD% AND %Shorthaul%;     FD\_short\_r1 is legal;     FD\_r1 is legal; end |
> |  | rule FD\_r1 =     %X% = 7; end |
> |  | rule FD\_long\_r1 =     %Y% > 5; end |
> |  | rule FD\_short\_r1 =     %Z% < 3; end |
> |  | IfFD\_longhaul is valid (the valid expression is true) and FD\_shorthaul is not valid, then the sub-rules FD\_r1 and FD\_long\_r1 are valid but FD\_short\_r1 is invalid. |
>
> Penalties and quality rules
>
> The expression of rules are in most cases written on the form:something1  inequality  something2
>
> |  |  |
> | --- | --- |
> | Example 1 | rule a\_rule =     %something% <= 2:45; end  The limit where a rule becomes illegal is exact: 2:45 is allowed but 2:46 is illegal. |
>
> To make the limit of a rule softer, you can define a penalty value to the rule. The penalty becomes higher the closer the expression value gets to the limit of the rule. The penalty value can be used by optimizers to get better solution quality.
>
> When used with penalty, therule\_condition syntax is:
>
> |  |  |  |
> | --- | --- | --- |
> | rule\_condition | ::= | expr inequality expr |
> | inequality | ::= | <= | < | > | >= |
>
> To define a penalty for a rule, there are three constants:min\_penalty, max\_penalty and delta. They are all optional.
>
> |  |  |  |
> | --- | --- | --- |
> | delta | ::= | delta = ( \_ | NUMBER | reltimeconst ) |
> | min\_penalty | ::= | min\_penalty = ( \_ | NUMBER ) |
> | max\_penalty | ::= | max\_penalty = ( \_ | NUMBER ) |
>
> |  |  |
> | --- | --- |
> | Example 2 | rule a\_rule =     %something% <= 2:45;     delta = 0:15;     min\_penalty = 50;     max\_penalty = 100; end |
> |  | The penalty is a linear function. If%something% is greater than 2:45, the rule is illegal. The rule will result in a penalty if %something% is close to the limit of 2:45, within the distance of delta according to the figure below. |
> |  |  |
> |  | A few examples from the figure above:  %something% = 2:30 penalty\_value = 50 %something% = 2:31 penalty\_value = 53 %something% = 2:45 penalty\_value = 100 %something% = 2:46 Rule failure |
>
> |  |  |
> | --- | --- |
> | Note | The Rave built-in functiontotal\_rule\_penalty is used to include the rule penalties in a cost function. |
>
> Rule violation cost
>
> A purely cost-based heuristic optimizer requires that each rule has a cost of violating the rule. Typically two cost ranges are used: a very high range to model severe operational infeasibilities, and another range that is magnitudes smaller to manage minor operational problems, like revenue loss.
>
> |  |  |
> | --- | --- |
> | Example | The following rules are defined for a heuristic cost-based optimizer. The first rule captures a simple infeasibility. The second rule exemplifies that certain rule violations are worse than others, and that the optimizer should trade severe rule violations for more simple ones. The third rule reflects a minor operational problem and is modelled in the lower cost range. |
> |  | %infeasibility\_cost% = 10000000;  rule inconsistency\_rule =      activity\_end\_station <>             next(leg(chain), activity\_start\_station);     cost = %infeasibility\_cost%; end  rule overlap\_rule =     activity\_end\_time <= next((chain), activity\_start\_time);     cost = 2 \* %infeasibility\_cost%; end  rule route\_rule =     valid %gps\_broken%;     %dont\_fly\_over\_water%;     cost = 2000; end |
>
> When compiling rule sets for an optimizer that requires rule costs, the Rave compiler enforces mandatory use of costs for all rules. If the optimizer does not use rule costs, any defined cost is ignored.
>
> Messages (failtext)
>
> In addition to regular comments (remarks), you can add rule failure messages that are available for report generation. These messages can also be used for constraints.
>
> |  |  |  |
> | --- | --- | --- |
> | failtext | ::= | failtext expr | failtext(lhs, rhs) = expr; |
> | lhs | ::= | formal\_arg |
> | rhs | ::= | formal\_arg |
>
> |  |  |
> | --- | --- |
> | Example | rule max\_trip\_duty\_days =     trip.%days% <= %max\_trip\_days%;     failtext concat("Not allowed to have ",        format\_int(trip.%days%, "%i "),         "in one trip."); end |
>
> Thelhs and rhs arguments correspond to the left-hand side and right-hand side in the rule or constraint condition (the types must match). For an example, see [Constraint failtext](Definitions.06.04.html#40779 "Constraints").
>
> Rule failures
>
> Some optional rule attributes are related to rule failures. How the attribute values are used is defined by the application.
>
> |  |  |
> | --- | --- |
> | • | failobject: a string that can be used by applications to find information about the chain that caused a legality check to fail. |
>
> |  |  |
> | --- | --- |
> | • | severity: an integer indicating the severity of a rule failure. |
>
> |  |  |
> | --- | --- |
> | • | deadline: an AbsTime variable indicating the deadline for attending to a rule failure. Typically used in a crew tracking application, |
>
> |  |  |
> | --- | --- |
> | • | overshoot\_min\_limit: integer or RelTime indicating a lower limit for rule relaxation. Used when excepting rules in applications. |
>
> |  |  |
> | --- | --- |
> | • | overshoot\_max\_limit: integer or RelTime indicating an upper limit for rule relaxation. Used when excepting rules in applications. |
>
> |  |  |
> | --- | --- |
> | See also | TheRuleFail class in the Rave Python API documentation. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Definitions.06.02.html)  | [next](Definitions.06.04.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |