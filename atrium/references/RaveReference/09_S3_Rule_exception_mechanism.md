## Rule exception mechanism

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Modelling_Info.10.3.html)  | [next](App_Rave_Compiler.11.1.html) |

> Rule exception mechanism
>
> Sometimes you want to avoid applying one or more rules that make a chain illegal. This is possible with the rule exception mechanism.
>
> |  |  |
> | --- | --- |
> | Example | Crew member Smith exceeds his block time limit by ten minutes. Instead of changing Smith’s roster you can create a rule exception for him. The rule exception applies only to Smith and only for a relevant period of time within his roster. |
>
> In order to use the rule exception mechanism you need to do two things:
>
> |  |  |
> | --- | --- |
> | 1. | Configure your system to use the rule exception mechanism. See[Rule exceptions](Definitions.06.03.html#48082 "Rules"). Contact your service manager for more information. |
>
> |  |  |
> | --- | --- |
> | 2. | Modify your rules in such a way that they know how to behave when an exception is applied to them. If you do not do this, the rule will not change when rule exceptions are activated. |
>
> Rules can have two types of behaviour when exceptions are created:
>
> |  |  |
> | --- | --- |
> | • | The rule is made less restrictive for the period of the exception. |
>
> |  |  |
> | --- | --- |
> | • | The rule is turned off for the period of the exception. |
>
> The examples in[Different scopes for exceptions](#40613 "Rule exception mechanism") show how these different types of behaviour could be included in a Rave rule definition.
>
> |  |  |
> | --- | --- |
> | Note | Normally the expressionsx < 6 and x <= 5 are equivalent. However, if you use rule exceptions the expression x < 6 + %waive\_extension% will not work. When creating the rule exception, the system calculates the difference between the actual value (10 for example) and the limit (6) and writes the result (4) in the rule\_exceptions etable as waive\_extension. The rule is then evaluated as 10 < 6 + 4, which is always false. Therefore, always use less or equal (for example x <= 5 + %waive\_extension%). |
>
> Different scopes for exceptions
>
> The scope of the exception defines the part of the roster where the exception is applied. It is tightly related to the scope of the rule. For example, if a rule works on the month level, then the scope of the exception should also be at the month level. The various possible scopes should therefore usually match your own Rave levels. In the example below the scope is the month level.
>
> |  |  |
> | --- | --- |
> | Example | Modifying a monthly block time rule.  Suppose that you want to modify the following rule to work with rule exceptions.  Rule month\_max\_block\_time   %month\_block\_time% <= %month\_max\_block\_time%;   REMARK "Maximum block time allowed in one month."; END |
> |  | Version 1 - Changing the limit  It is usually more preferable to modify an illegal rule than to switch it off completely. You can do this with rules that are expressed inINTEGER, RELTIME or ABSTIME form. |
> |  | Rule month\_max\_block\_time   %month\_block\_time% <= %month\_max\_block\_time% +                         %month\_extension\_rel%;   REMARK "Maximum block time allowed in one month.";   startdate = %month\_waive\_sdate%;   enddate = %month\_waive\_edate%; END |
> |  | The dictionary variables%month\_extension\_rel%, %month\_waive\_sdate% and %month\_waive\_edate% will be defined as part of your rule exception configuration. You should not define them yourself. However, note that they may have different names in your implementation. |
> |  | The scope of the rule exception is determined by the%month\_extension\_rel%, %month\_waive\_sdate% and %month\_waive\_edate variables. Similar variables should exist for the other rule exception scopes. So, if you have a trip level defined you should also have a scope defined with dictionary variables %crr\_extension\_rel%, %crr\_waive\_sdate% and %crr\_waive\_edate%. |
> |  | ForABSTIME and RELTIME rules the limit is changed via the %<scope>\_extension\_rel% variable. For integer rules the corresponding set of %<scope>\_extension\_int% variables should be used instead. |
> |  | Note that theextension\_int and extension\_rel variables are always positive. This means that you need to account for the correct adjustment in the rule definition itself. For a less than rule (as in the example) you should add the extension and for a greater than rule you should subtract the extension. |
> |  | Version 2 - Turning off the rule  Some rules may not be easy to modify when they create an illegality. Those rules can instead be switched off for the scope of the exception. To do this you should write such rules in the following way: |
> |  | Rule month\_max\_block\_time   VALID NOT %month\_waive\_rule%;   %month\_block\_time% <= %month\_max\_block\_time%;   REMARK "Maximum block time allowed in one month.";   startdate = %month\_waive\_sdate%;   enddate = %month\_waive\_edate%; END |
> |  | The dictionary variables %month\_waive\_rule%, %month\_waive\_sdate% and %month\_waive\_edate% will be defined as part of your rule exception configuration. You should not define them yourself. However, they may have different names in your implementation.  As with the previous example, similar variables should exist for the other rule exception scopes. |
>
> Controlling addition of rule exceptions
>
> Some applications, for example Crew Tracking, allow users to add rule exceptions from the GUI. In that case the Rave implementation can include a Rave function callednon\_except\_regexps, typically a table, that returns a list of regular expressions. All rules matching the expressions should be excluded from the rule exception feature. That is, it should not be possible to add exceptions to them.
>
> |  |  |
> | --- | --- |
> | Example | /\* List regexps for all rules that shouldn't have any rule exceptions \*/ table non\_except\_regexps(Int entry\_nr) =   entry\_nr -> %non\_except\_regexp%; 1 -> "qualifications.trip\_crew\_has\_ac\_quals"; 2 -> "qualifications.trip\_crew\_has\_airport\_quals"; 3 -> "qualifications.trip\_crew\_has\_cat\_quals"; ... - -> void\_string; |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Modelling_Info.10.3.html)  | [next](App_Rave_Compiler.11.1.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |