## Multiple implementations

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.2.html)  | [next](Modules.07.4.html) |

> Multiple implementations
>
> Sometimes the same module needs to be implemented in several different ways. For example, one for short haul and one for long haul. Rave allows multiple implementations of the same module. One module implementation is marked as root module, by addingroot in front of module in the header. Other implementations of this module can either reimplement the module from scratch, or inherit all definitions from another implementation and redefine them. Inheritance can be made in any number of levels.
>
> An import statement is always followed by a root module name. Which implementation that is actually used is determined when building the rule set.
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Inheritance](#22050 "Multiple implementations") |
>
> |  |  |
> | --- | --- |
> | • | [Partial redefinition](#22093 "Multiple implementations") |
>
> |  |  |
> | --- | --- |
> | • | [Pure interface modules](#22154 "Multiple implementations") |
>
> Inheritance
>
> A child module inherits all definitions from its parent module. Definitions that need to be changed in the new implementation are redefined, and new definitions can also be added.
>
> The syntax for the file header is different for parent modules:
>
> |  |  |  |
> | --- | --- | --- |
> | fileheader | ::= | root module module\_ident |
>
> |  |  |
> | --- | --- |
> | Example | For example, you can select therest module to be the root module by changing its header to:  root module rest ... |
> |  | In the new module implementationrest\_sh you can redefine the %long\_rest% time to be only nine hours:  module rest\_sh inherits rest   redefine %long\_rest% = parameter 9:00;   .... |
>
> In the example, the child module needs to usemodule\_type to specify the parent module.
>
> |  |  |  |
> | --- | --- | --- |
> | module\_type | ::= | inherits module\_ident |
>
> Definitions that are redefined have to be marked with the wordredefine. This prevents the value of an inherited definition from being overridden by mistake, and makes a clear distinction between defining a new definition and redefining an inherited definition. The inherited variable %length% in the example, as introduced in [Basic module](Modules.07.2.html#27442 "Basic module"), will be based on the redefined long rest of nine hours in the rest\_sh module.
>
> redefine is combined with the export status. You can keep the same export status when inheriting, or change it to a more visible status. For example, redefining a local variable into an exported.
>
> |  |  |
> | --- | --- |
> | Example | redefine export %long\_rest% = 9:00; |
>
> Partial redefinition
>
> It is possible to redefine only part of a definition in an inheriting module. If not all parts of a definition are redefined, then the missing parts are inherited from the root module. For example, a parameter value may be redefined while its comment is inherited, or its comment is redefined and its value inherited. For parameters, rules, and variables a place holder,"\_", is needed to inherit the value and the body respectively. For group definitions, the same place holder can be used as the first group member to inherit the group members from the root module.
>
> |  |  |  |
> | --- | --- | --- |
> | par\_const | ::= | \_ |
> | var\_body | ::= | \_ |
> | rule\_body | ::= | \_ |
> | groupmem | ::= | \_ |
>
> |  |  |
> | --- | --- |
> | Example | root module a\_module   %a% = parameter 5 remark "a comment";   %b% = parameter 10 maxvalue 10;   %x% = parameter 1;   %y% = parameter 2;   group grpZ = %x%,%y%; |
> |  | module a\_child\_module inherits a\_module   redefine %a% = parameter \_ remark "another comment";   redefine %b% = parameter 20; /\* compilation error \*/   %z% = parameter 3;   redefine group grpZ = \_, %z%; |
> |  | %a% in a\_child\_module has been given another comment, while its value 5 is unchanged. The redefinition of %b% gives a compilation error, since the new value of 20 exceeds the inherited maximum value of 10.  GroupgrpZ is redefined to include the %x% and %y% parameters from the root module, as well as the new %z% parameter. |
>
> Comments for variables, tables, sets, and rules are also inherited. For rules, if each valid expression (delta, max\_penalty, min\_penalty) or the expression itself is not redefined, it is partially inherited. Notice that you have to redefine a value to its default setting to avoid partial inheritance.
>
> Pure interface modules
>
> A root module does not have to implement all its definitions. If a variable is not implemented, the inheriting/implementing child modules are forced to implement that variable. Levels and iterators are other definitions that can be left unimplemented.
>
> |  |  |  |
> | --- | --- | --- |
> | level\_def | ::= | gexport level ident ; |
> | iter\_def | ::= | gexport iterator ident ; |gexport iterator ident =   [remark\_semi]  end |
> | var\_body | ::= | data\_type |
> | rule\_def | ::= | gexport rule [ponoff] rule\_ident ; |
> | constraint\_def | ::= | gexport constraint [ponoff] ident ; |
>
> A pure interface of the rest module could look like:
>
> root module rest  
>   export %length% = Reltime;
>
> All child modules of rest must define%length% with the data type reltime.
>
> This construction is well suited for defining multiple implementations.
>
> ![](images/Multiple_implementations.png)
>
> The root module can contain everything that is common to its child modules, leaving some definitions unimplemented. The definitions in the child modules can then deal with specific cases and can use the common definitions in the root module.
>
> |  |  |
> | --- | --- |
> | Example | A standard module using levels and iterators can be implemented without knowing the names of the corresponding definitions in the specific rule set. |
> |  | root module carmen\_std\_module level carmen\_trip; <implementation of the standard module using carmen\_trip> |
> |  | module std\_module\_config inherits carmen\_std\_module import levels; redefine level carmen\_trip = levels.crr; |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.2.html)  | [next](Modules.07.4.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |