## Rave run-time statistics

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Modelling_Info.10.2.html)  | [next](App_Modelling_Info.10.4.html) |

> Rave run-time statistics
>
> It is possible to obtain detailed information on how the rules are run in Crew Pairing Optimizer by setting the Crew Pairing Optimizer parametercrc\_runtime\_statistics to true. The parameter sets Crew Pairing Optimizer in a mode where all calls to the rules are logged and clocked. When an optimization job is completed, two reports are made available. These reports contain statistical information such as:
>
> |  |  |
> | --- | --- |
> | • | the number of times a rule was legal |
>
> |  |  |
> | --- | --- |
> | • | the number of times a rule was illegal |
>
> |  |  |
> | --- | --- |
> | • | the CPU time spent in a rule. |
>
> The files containing the reports are viewed with the commandLog Files Manager. Each file is named using the name of the optimization job followed by the extensions .crc\_con and .crc\_gen. The .crc\_gen file contains statistics from the generation phase of Crew Pairing Optimizer, while .crc\_con belongs to the connection matrix setup phase.
>
> The following is an example of a Rave run-time statistics report:
>
> |  |  |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- | --- |
> | Rule | APC  pass | APC  fail | APC  msec | Total  pass | Total  fail | Total  msec |
> | max\_duty\_per\_day | 2660 | 0 | 0 | 2680 | 10 | 0 |
> | min\_days\_off | 2660 | 0 | 100 | 2690 | 0 | 100 |
> | rest\_after\_duty | 2680 | 10 | 100 | 2680 | 10 | 100 |
> | max\_flight\_hours\_per\_month | 2680 | 0 | 200 | 2690 | 0 | 200 |
> | max\_consecutive\_duty | 2680 | 0 | 0 | 2690 | 0 | 0 |
>
> For each rule there are six categories of statistics:
>
> APC pass
>
> Number of times the rule was found legal when the rule system is used as in a normal optimization job. For example, when a rule has been found illegal, dynamic sorting of rules and an immediate return from the rule system are applied.
>
> APC fail
>
> Number of times the rule was found illegal under the same circumstances as in theAPC pass column described above.
>
> APC msec
>
> CPU time used by the rule under the same circumstances as in theAPC pass column described above.
>
> Total pass
>
> Number of times the rule is found legal when Rave runs all rules in every call.
>
> Total fail
>
> Number of times the rule is found illegal when Rave runs all rules in every call.
>
> Total msec
>
> The amount of CPU time the rule uses when Rave runs all rules in every call.
>
> The report files are created in the dictionary:$CARMTMP/logfiles/crc\_runstat.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Modelling_Info.10.2.html)  | [next](App_Modelling_Info.10.4.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |