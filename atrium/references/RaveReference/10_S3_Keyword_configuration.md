## Keyword configuration

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Rave_Compiler.11.3.html)  | [next](Reverse.html) |

> Keyword configuration
>
> The configuration of the Rave compilerccrc is given by XML files containing information about keywords, contexts, transforms, etc. The document type definition resides in the $CARMSYS/data/crc/config.dtd file.
>
> |  |  |
> | --- | --- |
> | Example | This example shows an XML file that registers two keywords, one context and one transform:  <?xml version="1.0" standalone="no" ?> <!DOCTYPE ConfigDefinitions SYSTEM "{URI to file config.dtd}">  <ConfigDefinitions>  <Keyword name="arrival" type="abstime"      dependency="atom" function="rave\_arrival">   </Keyword>  <Keyword name="aircraft\_change" type="bool" voidy="true"     dependency="atom" function="rave\_aircraft\_change">     <Range level="atom" backward="0" forward="1"       parentLevel="chain">     </Range>   </Keyword>  <Context name="crew\_chains"     function="rave\_context\_crew\_chains">   </Context>  <Transform name="leg\_ref" dependency="atom"     context="crew\_chains" fromSegment="false" explosion="5"     function="rave\_transform\_leg\_ref">   </Transform> </ConfigDefinitions> |
>
> The first keyword has the namearrival in the Rave code and it has the data type abstime. The dependency is atom, meaning that the arrival keyword is an attribute on the atomic level object. The call-back function to the application is called rave\_arrival.
>
> The second keyword,aircraft\_change, has a sub-element Range describing that this keyword uses the current flight (looking zero flights backward) and next flight (one flight forward) to figure out if there is an aircraft change. This keyword can also return void if it is impossible to answer yes or no to the question.
>
> The registered contextcrew\_chains is a standard context with call back function rave\_context\_crew\_chains.
>
> Theleg\_ref transform is applied on an atomic level iteration group. Each element in the input is transformed into approximately five elements that belong to the previously registered context crew\_chains. It is the responsibility of the application programmer that the specified context includes all elements returned by the transformation function.
>
> Keywords, transforms, and contexts can be marked as deprecated, by using thedeprecated attribute of the XML configuration. Using deprecated entries generates a warning message when the rule set is compiled.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Rave_Compiler.11.3.html)  | [next](Reverse.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |