## Complete syntax

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Syntax.09.12.html)  | [next](App_Modelling_Info.10.1.html) |

> Complete syntax
>
> The Rave grammar rules are sorted alphabetically, except for the starting rule that is placed first. The BNF notation is explained in[BNF notation](Conventions.html#75250 "Conventions").
>
> |  |  |  |
> | --- | --- | --- |
> | toplevel | ::= | [fileheader] import\* def\* |
> | abstime\_const | ::= | month day year reltime\_const |month\_day year reltime\_const |day month year [ reltime\_const ] |day month\_year [ reltime\_const ] |
> | accumulator | ::= | gexport accumulator acc\_ident  (formal\_args) =    expression ;    [iterator = iter\_ident ;]    (attribute)\*  end |
> | acc\_ident | ::= | ident |
> | additive | ::= | + |- |
> | anypar | ::= | ( | ) |
> | assertion | ::= | booster\_assertion = expr |
> | attribute | ::= | attr\_ident [(formal\_args)] = expression ; |external expression ; |
> | attr\_ident | ::= | ident |
> | bool\_const | ::= | true | false |
> | bykeys | ::= | by ( keys ) |
> | cache\_args | ::= | cache\_range\_set | qual\_set\_ident |
> | cache\_range\_set | ::= | set (rconst, rconst) |
> | cluster | ::= | row \* |
> | clusters | ::= | clusters & cluster |cluster |
> | cond\_use | ::= | #if ident ( ( ident | NUMBER ) ) use\* end |
> | condition | ::= | expr |
> | conditions | ::= | exprs |
> | const | ::= | bool\_const |abstime\_const |reltime\_const |int\_const |string\_const |enum\_const |
> | constraint\_def | ::= | gexport constraint [ponoff] constr\_name =    [valid ;]    (foreach ;)\*    constr\_condition ;    [nonadditive(formal\_args) = expr ;]    [cost [(expr)] = expr ;]    [failtext ;]    [remark ;]    [group\_def]  end |
> | constr\_condition | ::= | sum(c\_set, expr) [where (expr)] c\_op c\_rhs  |count(c\_set) [where (expr)] c\_op c\_rhs |
> | constr\_name | ::= | ident |
> | c\_op | ::= | <= | >= | = |
> | c\_rhs | ::= | expr |
> | c\_set | ::= | context | transform\_ident |
> | constr\_name | ::= | ident |
> | context | ::= | ident |default\_context |current\_context |
> | data\_type | ::= | int | bool | string | reltime | abstime | qual\_enum\_ident |
> | dashes | ::= | - |dashes , - |
> | day | ::= | int\_const |
> | deadline | ::= | deadline = expr |
> | def | ::= | level\_def |var\_def |rule\_def |parent\_rule\_def |constraint\_def |table\_def |matrix\_def |set\_def |enum\_def |iter\_def |group\_def |filter\_def |require |use |assertion |
> | delta | ::= | delta = ( \_ | NUMBER | reltimeconst ) |
> | direction | ::= | forwards |backwards |
> | edefault | ::= | dashes -> results ; |
> | enum\_const | ::= | qual\_enum\_value |
> | enum\_def | ::= | gexport enum enum\_ident =    enum\_values    [ remark ; ]  end |
> | enum\_ident | ::= | ident |
> | enum\_value | ::= | ident remark ; |
> | enum\_values | ::= | enum\_values enum\_value  enum\_value |
> | exception | ::= | startdate = expr ; |enddate = expr ; |startday = expr ; |endday = expr ; |
> | expr | ::= | qual\_var\_ident [pexprs] |keyword [pexprs] |function [pexprs] |const |context ( context , expr ) |( expr ) |expr multiplicative expr |expr additive expr |expr relational expr |expr logical expr |expr membership qual\_ident |if expr then expr else expr |+ expr |- expr |not expr |trav\_ident ( transform\_ident ) |trav\_ident (trav\_key, expr) [trav\_spec] |trav\_ident (trav\_key [trav\_spec], expr ) |trav\_ident0 (trav\_key) [trav\_spec] |trav\_ident0 (trav\_key [trav\_spec]) |trav\_cat |
> | exprs | ::= | exprs , expr |expr |
> | extfname | ::= | expr |
> | failtext | ::= | failtext expr | failtext (lhs, rhs) = expr ; |
> | failobject | ::= | failobject =  expr |
> | fieldname | ::= | string |ident |
> | fileheader | ::= | module module\_ident [module\_type] |root module module\_ident |root rule set module\_ident; |
> | filter\_def | ::= | gexport filter filter\_ident = qual\_level\_ident ( expr ) ; |
> | filter\_ident | ::= | ident |
> | foreach | ::= | foreach lvar in foreach\_set [alias(expr)] [ispec] |
> | foreach\_set | ::= | set\_ident | enum\_ident | range\_set |
> | formal\_arg | ::= | data\_type ident [cache cache\_args] |
> | formal\_args | ::= | formal\_args , formal\_arg |formal\_arg |
> | from | ::= | from ( trav\_point [where] ) |from ( current ) |
> | function | ::= | ident |
> | gexport | ::= | [redefine] [[global] export] |
> | groupmem | ::= | qual\_ident |
> | groupmems | ::= | groupmems , groupmem |groupmem |
> | group\_def | ::= | group group\_ident = [groupmems] [remark]; |group group\_ident [remark] ; |
> | group\_ident | ::= | ident |
> | hour | ::= | int\_const |
> | ident | ::= | One or more characters:A-Z, a-z, 0-9 and underscore are allowed. |
> | import | ::= | import module\_ident ; |
> | inequality | ::= | <= |< |> |>= |
> | int\_const | ::= | one or more digits,0-9 |
> | ispec | ::= | where (expr) [while (expr)] |while (expr) [where (expr)] |
> | iter\_def | ::= | gexport iterator iter\_ident ; |gexport iterator iter\_ident =    [remark\_semi]  end  |gexport iterator iter\_ident =     partition ( qual\_ident ) [bykeys]    [remark\_semi]  end  |gexport iterator iter\_ident =    qual\_iter\_ident ; |
> | iter\_ident | ::= | ident |
> | key | ::= | expr |map ( trav\_key , keys ) |
> | keys | ::= | key , keys |key |
> | keyword | ::= | ident |
> | let | ::= | ident = expr |
> | lets | ::= | lets , let |let |
> | level\_body | ::= | when ( bool\_const ); |(is\_first|is\_last) (qual\_ident) when (expr); |
> | level\_def | ::= | gexport level ident ; |gexport level level\_ident =     level\_body    [remark ;]  end  |gexport level level\_ident = qual\_ident ; |
> | level\_ident | ::= | ident |
> | lhs | ::= | formal\_arg |
> | local\_var | ::= | let lets ; |
> | logical | ::= | and |and2 |or |or2 |
> | lvar | ::= | ident |
> | matrix\_def | ::= | matrix matrix\_ident [ pformal\_args ] =    [alias lets ;]    condition , condition -> result\_var;    test\_cases ;    matrix\_row+  end |
> | matrix\_ident | ::= | ident |
> | matrix\_outcome | ::= | expr |- |
> | matrix\_outcomes | ::= | matrix\_outcomes , matrix\_outcome |matrix\_outcome |
> | matrix\_row | ::= | test\_case ; matrix\_outcomes ; |
> | max\_penalty | ::= | max\_penalty = ( \_ | NUMBER ) |
> | min\_penalty | ::= | min\_penalty = ( \_ | NUMBER ) |
> | membership | ::= | [not] in |
> | minute | ::= | int\_const |
> | module | ::= | module\_ident |\_topmodule |
> | module\_ident | ::= | ident |
> | module\_type | ::= | inherits module\_ident |
> | month | ::= | jan | feb | mar | apr | may | jun | jul | aug | sep | oct | nov | dec |
> | month\_day | ::= | a month followed by a day without intervening space. |
> | month\_year | ::= | a month followed by a year without intervening space. |
> | multiplicative | ::= | \* |/ |mod |
> | NUMBER | ::= | an integer in the range -2,147,483,648 to +2,147,483,647 |
> | opt\_default | ::= | [default expr] |
> | opt\_sep | ::= | [, string\_const] |
> | outcome | ::= | expr |
> | outcomes | ::= | outcomes , outcome |outcome |
> | overshoot\_max\_limit | ::= | overshoot\_max\_limit = expr |
> | overshoot\_min\_limit | ::= | overshoot\_min\_limit = expr |
> | parent\_rule\_def | ::= | gexport rule [ponoff] rule\_name =    [valid ;]    [module .] rule\_name is legal ;    [remark "text" ;]  end |
> | par\_body | ::= | parameter par\_const [par\_limit] |
> | par\_const | ::= | sign\_const |\_ |
> | par\_def | ::= | gexport [durable] var\_ident =    par\_body    [remark ] ; |
> | par\_limit | ::= | minvalue par\_const |maxvalue par\_const |minvalue par\_const maxvalue par\_const |maxvalue par\_const minvalue par\_const |
> | patfield | ::= | fieldname |anypar fieldname , fieldname anypar |relop fieldname |
> | patfields | ::= | patfields , patfield |patfield |
> | pexprs | ::= | ( exprs ) |
> | pformal\_args | ::= | ( formal\_args ) |
> | ponoff | ::= | ( (on | off) ) |
> | prim\_expr | ::= | function [pexprs] |void ( data\_type ) |context ( context , expr ) |
> | qual\_enum\_ident | ::= | [module . ] enum\_ident |
> | qual\_enum\_value | ::= | [module . ] enum\_value |
> | qual\_ident | ::= | [module . ] ident |
> | qual\_iter\_ident | ::= | [module . ] iter\_ident |
> | qual\_level\_ident | ::= | [module . ] level\_ident |
> | qual\_matrix\_ident | ::= | [module . ] matrix\_ident |
> | qual\_rule\_ident | ::= | [module . ] rule\_name |
> | qual\_set\_ident | ::= | [module . ] set\_ident |
> | qual\_var\_ident | ::= | [module . ] var\_ident |
> | range | ::= | anypar sign\_const , sign\_const anypar |relop sign\_const |relop sign\_const or relop sign\_const |relop sign\_const and relop sign\_const |
> | range\_set | ::= | set (start, end [, step]) |
> | rconst | ::= | [+ | - ] const |
> | relational | ::= | = |<> |< |<= |> |>= |
> | relop | ::= | <> |< |<= |> |>= |
> | reltime\_const | ::= | hour : minute |
> | remark | ::= | remark role\_remarks |
> | remark\_semi |  | remark ; |
> | require | ::= | require string |
> | resfield | ::= | fieldname opt\_default |traverser\_ident ( fieldname opt\_sep )  opt\_default |
> | resfields | ::= | resfields , resfield |resfield |
> | result\_var | ::= | gexport [durable] [data\_type] var\_ident |
> | result\_vars | ::= | result\_var , result\_vars |result\_var |
> | results | ::= | result, results | result |
> | rhs | ::= | formal\_arg |
> | role | ::= | ident |
> | role\_remark | ::= | [role] [+] string |
> | role\_remarks | ::= | role\_remark , role\_remarks |role\_remark |
> | row | ::= | test\_cases -> outcomes ; |
> | rule\_condition | ::= | expr inequality expr |
> | rule\_def | ::= | gexport rule [ponoff] rule\_name =    [valid ;]    (exception ;)\*    (rule\_condition | \_);    [delta ;]    [cost = expr;]    [max\_penalty ;]    [min\_penalty ;]    [failtext ;]    [failobject ;]    [severity ;]    [deadline ;]    [overshoot\_min\_limit ;]    [overshoot\_max\_limit ;]    [remark ;]  end |gexport rule [ponoff] rule\_name ;  Rule definition statements can occur in any order. |
> | rule\_name | ::= | ident |
> | sep | ::= | string |
> | setcont | ::= | [parameter] set\_body [remark]  external data\_type setextfname .  fieldname [remark] |
> | setextfname | ::= | ( expr ) |qual\_var\_ident [pexprs] |keyword [pexprs] |string |
> | set\_body | ::= | set\_body , sign\_const |sign\_const |
> | set\_def | ::= | gexport set set\_ident = setcont ; |
> | set\_ident | ::= | ident |
> | severity | ::= | severity = expt |
> | sign\_const | ::= | [+ | - ] const |qual\_enum\_ident |
> | string\_const | ::= | string+ |
> | string | ::= | A sequence of characters enclosed in". All printable ISO-8859-1 characters or UTF-8 characters can be used except these: " \ newline  The following escape combinations can be used:\", \\, \n (newline), and \t (tab) |
> | table\_def | ::= | table table\_ident [pformal\_args] =     [alias lets ;]     conditions -> result\_vars ;     tablecont  end |
> | table\_ident | ::= | ident |
> | tablecont | ::= | clusters |external [data\_type] extfname ;  patfields -> resfields ;  [edefault]  [remark\_semi] |
> | test\_case | ::= | sign\_const |- |y |n |range |
> | test\_cases | ::= | test\_cases , test\_case |test\_case |
> | text | ::= | One or more characters in ISO-8859-1 |
> | to | ::= | to ( trav\_point [where] ) |to ( current ) |
> | towhile | ::= | to |while |
> | transform\_ident | ::= | ident |
> | trav\_ident | ::= | sum | avg |max | min |all | any |first | last |next | prev |earliest | latest |to |
> | trav\_ident0 | ::= | count |is\_first | is\_last |
> | trav\_cat | ::= | cat (trav\_key, ident, ident [sep])   [trav\_spec] |cat (trav\_key [trav\_spec], ident, ident,   [sep]) |
> | trav\_key | ::= | qual\_level\_ident ( expr ) |transform\_ident |
> | trav\_point | ::= | first |last |next |prev |
> | trav\_spec | ::= | from [towhile] [where] |towhile [where] |where [while] |
> | use | ::= | use module\_ident | cond\_use; |
> | valid | ::= | valid expr |
> | var\_body | ::= | data\_type |expr |\_ |
> | var\_def | ::= | gexport [durable] var\_ident [pformal\_args]=    [ local\_var ]    var\_body    [remark ] ; |
> | var\_ident | ::= | % one or more characters, % is not legal % |
> | where | ::= | where ( expr ) |
> | while | ::= | [direction] while ( expr ) |
> | year | ::= | int\_const |

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](App_Syntax.09.12.html)  | [next](App_Modelling_Info.10.1.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |