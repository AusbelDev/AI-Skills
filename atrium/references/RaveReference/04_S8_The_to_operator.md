## The "to" operator

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.08.html)  | [next](Expressions.05.10.html) |

> The "to" operator
>
> Theto operator is similar to a traverser, but requires a one-to-one mapping transform as its first argument. It goes from a data object in one context to a data object in another context, and does a calculation in that context.
>
> |  |  |
> | --- | --- |
> | Example | Instead of:  %ref\_plan\_work\_time% =     max( plan\_1\_crew\_first\_activity, %tot\_work\_time% );     /\* max of one value does not make sense \*/  you can write:  %ref\_plan\_work\_time% =     to( plan\_1\_crew\_first\_activity, %tot\_work\_time% ); |
>
> CARMSYS configuration
>
> An application must inform Rave that a transform is suited for use with theto operator via the Rave configuration file. This configuration cannot be modified in CARMUSR.
>
> |  |  |
> | --- | --- |
> | Example | The following definition is located in$CARMSYS/data/crc/GPC/config.xml. The value of the toSegment attribute is true, which indicates that the transform can be used with the to operator. |
> |  | <Transform name="plan\_1\_crew\_first\_activity"   dependency="chain"   context="plan\_1\_sp\_crew"   explosion="1"   toSegment="true"   function="crc\_dom\_segment\_reference\_plan\_1\_assignment">  <Remark text="The corresponding crew in reference plan 1"/> </Transform> |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.08.html)  | [next](Expressions.05.10.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |