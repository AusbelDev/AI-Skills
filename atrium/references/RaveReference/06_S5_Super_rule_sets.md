## Super rule sets

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.5.html)  | [next](Tools.html) |

> Super rule sets
>
> By using root modules and inherited modules, you can create two or more variants of rule sets that differ in their implementations. With a super rule set, you can create one large rule set that combines these variants. This makes it possible to have all variants loaded into an application at the same time.
>
> A super rule set can be regarded as a special type of module and is defined using this syntax in the file header:
>
> root rule set module\_ident;
>
> In the following example, a super rule set namedTracking is defined:
>
> |  |  |
> | --- | --- |
> | Example | root rule set Tracking; if crew.%is\_cabin\_crew% or trip.%is\_open\_cabin\_trip% then   use Tracking\_Cabin; else   use Tracking\_Cockpit; end |
>
> The condition(s) that decide which implementation to use must bechain or const dependent and may only refer to definitions from the first implementation (Tracking\_Cabin in the example above). That way an implementation is chosen for the current chain. When jumping to another chain within an evaluation, the conditions are checked again in order to use the correct implementation.
>
> The super rule set contains the union of all the Rave definitions of all the rule sets. The Rave compiler ensures that all definitions with the same name have the same signature. Note that this is normally enforced by the root/inherit modules compilation, but it is also possible to add other definitions not declared in a root module.

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Modules.07.5.html)  | [next](Tools.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |