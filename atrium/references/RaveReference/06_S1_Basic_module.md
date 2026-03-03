## Basic module

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.1.html)  | [next](Modules.07.3.html) |

> Basic module
>
> |  |  |  |
> | --- | --- | --- |
> | toplevel | ::= | [fileheader] import\* def\* |
> | fileheader | ::= | module module\_ident [module\_type] |
> | module\_ident | ::= | ident |
> | import | ::= | import module\_ident ; |
> | def | ::= | level\_def | var\_def | rule\_def |constraint\_def | table\_def | matrix\_def |set\_def | enum\_def | iter\_def | group\_def |filter\_def | require | use |assertion |
>
> A definition in a module is by default local and cannot be seen from other modules, except when exported. All definitions in Rave are preceded by the non-terminalgexport, see [Definitions](Definitions.06.01.html#21840 "Definitions").
>
> |  |  |  |
> | --- | --- | --- |
> | gexport | ::= | [redefine] [[global] export] |
>
> Theredefine keyword is explained in [Multiple implementations](Modules.07.3.html#22029 "Multiple implementations"). This optional prefix can be used to export any defined identifier. If an identifier is exported with only the export keyword, the identifier must be preceded by the name of the module where it is defined when it is accessed. This is called a qualified use. If global export is used, the module prefix is optional.
>
> |  |  |  |
> | --- | --- | --- |
> | qual\_enum\_value | ::= | [module . ] enum\_value |
> | qual\_enum\_ident | ::= | [module . ] enum\_ident |
> | qual\_var\_ident | ::= | [module . ] var\_ident |
> | qual\_rule\_ident | ::= | [module . ] rule\_ident |
> | qual\_iter\_ident | ::= | [module . ] iter\_ident |
> | qual\_level\_ident | ::= | [module . ] level\_ident |
> | qual\_matrix\_ident | ::= | [module . ] matrix\_ident |
> | qual\_set\_ident | ::= | [module . ] set\_ident |
> | qual\_ident | ::= | [module . ] ident |
>
> module is either a module identifier, or the predefined module name \_topmodule. The latter is used for modules without names. Variables that are not defined inside a module belong to \_topmodule.
>
> |  |  |  |
> | --- | --- | --- |
> | module | ::= | module\_ident |\_topmodule |
>
> Module interface
>
> The names and types of the exported definitions in a module constitute the interface of the module, and the interface is all other modules can see and use.
>
> The module concept provides a way of hiding details so that the implementation of a module can be changed without requiring any changes in other modules. This holds true as long as the interface stays the same.
>
> |  |  |
> | --- | --- |
> | Example | The following module contains definitions regarding rest times. |
> |  | module rest   import duty;  export %length% =     if(duty.%length% > 8:00) then %long\_rest%     else %short\_rest%;  %long\_rest% = parameter 10:00;   %short\_rest% = parameter 8:00;   .... |
>
> The module code should be placed in a file with the same name as the module, but with lower case letters. The header of a module file contains the name of the module. If a module uses other modules, these modules have to be imported. The import statements must be placed directly after the module’s header. In the example, therest module needs the duty module to implement its definitions. A definition in another module is referred to as module.definition. In the example, a reference is made to %length% in the duty module, duty.%length%. Notice that there are two definitions of %length%, one that belongs to the rest module and one that belongs to the duty module.
>
> Therest module exports the variable %length% for use in other modules. The variable %length% uses the locally defined variables %long\_rest% and %short\_rest%. Locally defined variables are only visible in the rest module.
>
> Variables defined by a table are exported in the same way.
>
> table a\_name =  
>   cond1, cond2 -> export Int %a\_variable%;  
>   ...
>
> Global export
>
> Commonly used definitions can be globally exported, which makes it unnecessary to specify the module from where they are exported.
>
> |  |  |
> | --- | --- |
> | Example | An example of globally exported definitions are the level definitions.  module levels   global export level leg = ...   global export level duty = ...   .... |
> |  | These allow us to write a duty module like  module duty   import levels;   export %length% = %end% - %start%;   %start% = first(leg(duty), departure);   %end%   = last (leg(duty), arrival);   .... |
> |  | leg and duty can be referred to without having to specify that they are defined in the levels module. Notice that the levels module still has to be imported. |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.1.html)  | [next](Modules.07.3.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |