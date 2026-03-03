## Improving the performance of Rave code

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Modelling_Info.10.1.html)  | [next](App_Modelling_Info.10.3.html) |

> Improving the performance of Rave code
>
> The following sections give suggestions on what to study when addressing performance problems in Rave code.
>
> |  |  |
> | --- | --- |
> | • | [Dependency of rules](#22085 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Range](#22089 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Caching](#46046 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Function caches](#36888 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Durable caches for variables](#37081 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Transforms](#41848 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Levels](#22152 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Number of rules](#22155 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Order of calculation in rules](#40597 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Complexity of rules](#46067 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Number of objects](#47515 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Vertical constraints](#22190 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Minimize the input to the optimizer](#22193 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Using the Column Generation method](#22196 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Tune the optimizer](#22202 "Improving the performance of Rave code") |
>
> |  |  |
> | --- | --- |
> | • | [Where statements in constraints](#22205 "Improving the performance of Rave code") |
>
> Dependency of rules
>
> Are the rules and variables attributes at the correct level, or are they evaluated on smaller objects than necessary?
>
> Making a rule unnecessarily leg-dependent will cause Rave to check the rule on every leg. Mixing dependencies may also affect caching, see[Caching](#46046 "Improving the performance of Rave code").
>
> Range
>
> The range of a variable or a rule is the set of level objects needed to evaluate it. For optimization runs, it is important that the range is as small as possible. If it is too large there will be a lot of unnecessary Rave evaluations. A leg rule or variable with a range of chain is the worst case: each time the value is computed on a leg you need attributes from all legs in the chain.
>
> |  |  |
> | --- | --- |
> | Example 1 | /\* Roster range \*/ %connection\_time1% = next(leg(roster), departure) - arrival;  /\* Duty range \*/ %connection\_time2% = next(leg(duty), departure) - arrival;  The second definition in this example is much better, since Rave will only need to recalculate the connection time if the duty changes instead of every time the roster changes. |
>
> |  |  |
> | --- | --- |
> | Example 2 | Time window calculations are examples of a type of definition that often get a bad range. A naive implementation that calculates the block time in 24 hours might look like this: |
> |  | %block\_in\_24\_h% =   let end\_24\_h = departure + 24:00;   sum(leg(chain), %block\_before%(end\_24\_h))     from (current) where (departure < end\_24\_h); |
> |  | Since the legs are always ordered in time, the computational complexity can be lowered usingwhile instead of where:  %block\_in\_24\_h% =   let end\_24\_h = departure + 24:00;   sum(leg(chain), %block\_before%(end\_24\_h))     from (current) while (departure < end\_24\_h); end |
> |  | The result is the same, but the range will be defined as "all legs up to the first one outside the time window" instead of "all legs to the end of the chain except the ones outside the time window". |
>
> Often domain knowledge is useful when trying to limit the range. If there always is at least a day off between trips, due to rules and levels,chain can be replaced with trip in example 2.
>
> Caching
>
> Examine code with a high number of calls. Are more calculations than necessary done? Could the number of calls be reduced by more efficient caching?
>
> Generally, only the value of a variable or a rule can be cached, not an expression that is part of a definition.
>
> |  |  |
> | --- | --- |
> | Example 1 | In the definition  %v% = %a% + sum(leg(duty), %b%);  thesum expression cannot be cached, but in the following definition it can be cached:  %sum% = sum(leg(duty), %b%); %v% = %a% + %sum%; |
>
> If an expression is used in more than one place it should be made a separate definition.
>
> Mixing dependencies in definitions may also cause caching problems.
>
> |  |  |
> | --- | --- |
> | Example 2 | %trip\_val% = sum(leg(trip), %leg\_val%); %leg\_val% =   if %trip\_property% then %leg\_property\_1% \* %factor%   else %leg\_property\_2% \* %factor%; |
> |  | In this example%leg\_val% has a trip range, since it depends on %trip\_property%. Every time the trip changes, %leg\_val% must be recomputed on each leg.  The solution is to move the use of%trip\_property% up to the trip level: |
> |  | %trip\_val% =    if %trip\_property% then sum(leg(trip), %leg\_val\_1%)   else sum(leg(trip), %leg\_val\_2%); %leg\_val\_1% = %leg\_property\_1% \* %factor%; %leg\_val\_2% = %leg\_property\_2% \* %factor%; |
> |  | Now the values of%leg\_val\_1% and %leg\_val\_2% can be cached and reused. If the trip changes, it will only have to be computed on added legs. |
>
> Function values are never cached, but you can create cache variables for the most common arguments.
>
> |  |  |
> | --- | --- |
> | Example 3 | %crew\_category\_trip\_start% = %crew\_category%(trip.%start%); |
>
> Context values, for example total block time in a certain context, can be cached and reused independently of any chain if such chain-independent variable is made available.
>
> |  |  |
> | --- | --- |
> | Example 4 | %sp\_total\_block% =   context(sp\_crrs, sum(chain\_set, %total\_block%)); |
>
> Sometimes external tables created by scripts can be used to cache certain values in a more efficient way. An example of this are values calculated on preassignments and history.
>
> Function caches
>
> It is possible to add a special annotation on a user-defined function to cache calls with specific arguments. This functionality should only be used after analysis of profiling runs, since the extra cache slots will use application memory. Function caches may even make program execution slower, if used inappropriately.
>
> The syntax is as follows:
>
> |  |  |  |
> | --- | --- | --- |
> | formal\_arg | ::= | data\_type ident [cache cache\_args] |
> | cache\_args | ::= | cache\_range\_set | qual\_set\_ident |
> | cache\_range\_set | ::= | set (rconst, rconst) |
> | rconst | ::= | [+ | - ] const |
>
> |  |  |
> | --- | --- |
> | Example | /\* Cache a function for the arguments 1, 2, and 3. \*/ %fun1%(int i cache set(1,3)) = ...  /\* Cache a function for the strings "CAB" and "COC" \*/ set category = "CAB", "COC"; %fun2%(string s cache category) = ... |
>
> Durable caches for variables
>
> The reserved worddurable gives a hint to some applications (for example Crew Pairing Optimizer) that they should cache a variable more efficiently. In particular, it should be possible to move an object, for example a leg, in between two trips and still keep the variable value.
>
> Before marking a variable asdurable, you should perform a performance analysis to find out if there are any candidates. First of all, the computations of this variable should be heavy and numerous. The dependency of the variable should be equal to the range (for example a leg variable not dependent on any other level object in the chain). Marking too many variables as durable increases memory usage significantly.
>
> Transforms
>
> The syntaxcount(ac\_rotations\_ref) generates much faster code than transform(ac\_rotations\_ref, count(leg\_set)). The last-mentioned syntax transforms are demanding to compute and should be avoided if possible.
>
> Levels
>
> The level structure is used a lot in all Rave evaluations, and that is why levels should be modelled with simple expressions. Too many levels will slow down the system no matter how little they are used. You should also avoid parallel level hierarchies if possible.
>
> Number of rules
>
> It can be a better approach to combine a few simple rules instead of using one slightly more complex.
>
> Order of calculation in rules
>
> Always check simple conditions first in rules. More complex conditions might not have to be calculated. For example, use thevalid statement in rules (calculated first) to check that you are within the planning period.
>
> |  |  |
> | --- | --- |
> | Example 1 | Consider for example a rule that limits the number of inexperienced crew on a leg. It uses a transform,equal\_trips, that returns all references to the same trip from different crew rosters:  rule max\_inexperienced =   count(equal\_trips where (%inexperienced%)) <= 1; end |
> |  | Avalid statement can make this much more efficient:  rule max\_inexperienced =   valid %inexperienced%;   count(equal\_trips where (%inexperienced%)) <= 1; end  Now the transform is only evaluated on the trips of inexperienced crew, rather than on every single trip. |
>
> The boolean operatorsand and or are order-dependent and the second operand will only be calculated if necessary.
>
> In the expression%x% and %y%, the variable %y% will only be evaluated if %x% is true. The opposite for disjunction: in the expression %x% or %y% the variable %y% will only be evaluated if %x% is false.
>
> |  |  |
> | --- | --- |
> | Note | This does not apply for multiplication. In the expression%x% \* %y% the variable %y% will always be evaluated, even if %x% is 0. |
>
> |  |  |
> | --- | --- |
> | Example 2 | By rewriting the expression  %weight%\*%cost%  to  if %weight%=0 then 0 else %weight%\*%cost%  you avoid calculating the right-hand side. |
>
> Complexity of rules
>
> You often get a better end result if you can rewrite a rule to be slightly more restrictive, but on the other hand less complex and faster.
>
> Number of objects
>
> Collect objects that never are spread in as large blocks as possible. For example, it is better to create a single ten-day activity compared to ten one-day activities.
>
> Using less objects makes it easier for both the optimizer and Rave and may improve the performance and memory consumption a lot.
>
> Vertical constraints
>
> Use as few vertical constraints as possible, as they affect both setup and optimization time.
>
> Minimize the input to the optimizer
>
> For example, there is no reason to allow trips/rosters that you would not accept in the final solution - even if they are formally legal.
>
> Using the Column Generation method
>
> There are more tips on how to write efficient code for the Column Generation method inCrew Pairing Optimizer Reference.
>
> Tune the optimizer
>
> Tuning the optimizer can give very big performance improvements. Crew Rostering comes with a self-tuning Python script that has proven efficient.
>
> Where statements in constraints
>
> Usingwhere statements where appropriate may improve performance with Crew Pairing Optimizer, since these are evaluated more efficiently than the corresponding if statement.
>
> |  |  |
> | --- | --- |
> | Example | The formulation  constraint ex1 =  foreach base in active\_bases;   sum(default\_context, %contribution%)        where (base = homebase) <= %my\_limit%; end  is more efficient than |
> |  | constraint ex2 = foreach base in active\_bases;   sum(default\_context, if base = homebase          then %contribution% else 0) <= %my\_limit%; end  as long as thewhere statement removes a significant part of the instances (more that approximately 70% of the number of instances). |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Modelling_Info.10.1.html)  | [next](App_Modelling_Info.10.3.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |