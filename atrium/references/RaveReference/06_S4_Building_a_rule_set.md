## Building a rule set

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.4.html)  | [next](Modules.07.6.html) |

> Building a rule set
>
> This section describes the following topics:
>
> |  |  |
> | --- | --- |
> | • | [Structure of a rule set](#32668 "Building a rule set") |
>
> |  |  |
> | --- | --- |
> | • | [Choosing modules](#22300 "Building a rule set") |
>
> |  |  |
> | --- | --- |
> | • | [Conditional use](#22373 "Building a rule set") |
>
> |  |  |
> | --- | --- |
> | • | [Backward compatibility](#22393 "Building a rule set") |
>
> Structure of a rule set
>
> A rule set is defined by a file called the top module of the rule set. The name of this file is also the name of the rule set. This file defines which modules that will be included in the rule set. When there is more than one implementation of a module the file also defines which of these implementations should be used.
>
> Choosing modules
>
> The top module contains one or moreuse statements. A use statement specifies which modules, or more precisely, which module implementations the rule set consists of.
>
> The syntax for ause statement is:
>
> |  |  |  |
> | --- | --- | --- |
> | use | ::= | use module\_ident | cond\_use; |
> | cond\_use | ::= | #if ident '(' ( ident | NUMBER ) ')'use\* end |
>
> See[Conditional use](#22373 "Building a rule set") for more information about conditional use statements. By using a module, all variables and rules defined in that module will become part of the rule set.
>
> When a module is implemented only once, theuse statement for that module is optional if the statement is included by an import somewhere else.
>
> |  |  |
> | --- | --- |
> | Example | module main   import rest;   import levels;   ... |
> |  | root module rest ... module rest\_sh inherits rest ... |
> |  | module levels ... module duty ... |
> |  | A rule set top file used to build a rule set containing the main module would look like this:  use main; use rest\_sh;  The second statement above says that the implementationrest\_sh should be included and used whenever the statement import rest is found. |
> |  | It is not necessary, but it is possible to have the clause  use levels;  since there is only one implementation oflevels and the module is imported by main module. |
> |  | By adding the clause  use duty;  the definitions in the duty module, not otherwise present, would be added to the rule set. |
>
> Conditional use
>
> The syntax for conditional use is:
>
> |  |  |  |
> | --- | --- | --- |
> | cond\_use | ::= | #if ( ident ) use\* end |
>
> A conditional use statement can be applied when a rule set is used for different phases of the planning process. One version might be used in manual planning and another in automatic planning, or you may also wish to have slightly different versions of the rule set for different crew categories, for example pilots and cabin crew.
>
> The conditional use makes it possible to alter the implementation of a module for different occasions.
>
> |  |  |
> | --- | --- |
> | Example | #if target(attribute)   use implementation\_l;   use ...; end |
>
> The statement checks if the target has the specified attribute and if so, the following implementations are used. There can be many targets representing, for example, the planning method and the process phase. Each target can also have several attributes. The targets and attributes are dependent on the system.
>
> Conditional use in a system
>
> When using Rave with tools such as Studio or Crew Pairing Optimizer, the target is available with the attribute set togpc or apc, respectively.
>
> |  |  |
> | --- | --- |
> | Example 1 | #if product(gpc)   use report\_module; end |
>
> A synonym forgpc is studio.
>
> The system version number is available as an attribute with numeric values.
>
> |  |  |
> | --- | --- |
> | Example 2 | #if version(12)   use v12\_specific\_module; end |
>
> Backward compatibility
>
> Before modules were introduced in Rave, rule sets were written in a single name space, possibly separated in several files withrequire. For backward compatibility and to enable easy and gradual migration, such a rule set may be used as a top module. That is, it is possible to have definitions of variables, etc. in a top module. These definitions are considered to be part of a special module called \_topmodule. The top module of a rule set consists of the top file as well as other files included with require:
>
> |  |  |  |
> | --- | --- | --- |
> | require | ::= | require string |
>
> The top module of the rule set may contain many files, but is seen as one single module. A definition in one file of the top module can be referred to in any other file of the top module.
>
> The top module can import modules and refer to them as usual and for migration purposes, modules can also import\_topmodule. Import statements in the top module have to be written in the beginning of the top module files.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.4.html)  | [next](Modules.07.6.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |