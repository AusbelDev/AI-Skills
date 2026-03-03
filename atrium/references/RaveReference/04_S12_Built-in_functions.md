## Built-in functions

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.12.html)  | [next](Expressions.05.14.html) |

> Built-in functions
>
> A number of built-in functions provide special services. Built-in functions return void if any of the arguments are void.
>
> Syntax
>
> The general syntax is:
>
> |  |  |  |
> | --- | --- | --- |
> | prim\_expr | ::= | function [pexprs] |void ( data\_type ) |
> | function | ::= | ident |
>
> The built-in functions can be grouped according to:
>
> |  |  |
> | --- | --- |
> | • | [Numerical functions](#23008 "Built-in functions") |
>
> |  |  |
> | --- | --- |
> | • | [Time functions](#23032 "Built-in functions") |
>
> |  |  |
> | --- | --- |
> | • | [Rule functions](#23201 "Built-in functions") |
>
> |  |  |
> | --- | --- |
> | • | [Format functions](#23203 "Built-in functions") |
>
> |  |  |
> | --- | --- |
> | • | [String functions](#33451 "Built-in functions") |
>
> |  |  |
> | --- | --- |
> | • | [Void functions](#50210 "Built-in functions") |
>
> |  |  |
> | --- | --- |
> | • | [Iterator functions](#23577 "Built-in functions") |
>
> |  |  |
> | --- | --- |
> | • | [CAPI functions](#43894 "Built-in functions") |
>
> Numerical functions
>
> The numerical functions are:
>
> abs(expr)
>
> expr may be integer or reltime, the result has the same type. Abs returns the absolute value of its argument.
>
> sqrt(expr)
>
> sqrt returns the integer square root of a given positive integer. A negative integer will result in a run-time error.
>
> nmax(expr1,expr2,...)  
> nmin(expr1,expr2,...)
>
> Returns the largest/smallest of its arguments (at least two). All data types are supported and all arguments must have the same type.
>
> Time functions
>
> In these functions the beginning of a week is considered to be midnight between Sunday and Monday. The time functions are:
>
> overlap(start1,end1,start2,end2)
>
> The arguments must either all be abstime, or all be reltime. The result is reltime. Overlap returns the amount of time that the two intervals[start1,end1] and [start2,end2] overlap.
>
> scale\_time(start,end,scale,start1,end1,scale1,...)
>
> This function can put different weighting of time during a day, for example to model extra compensation for unsocial working hours during night.
>
> The function returns a reltime value that is a scaled number of hours that overlaps an absolute time interval. After the three first required arguments (start,end,scale) follows any number of triplets (start1,end1,scale1,start2,end2,scale2...). start and end are abstimes, startN and endN are reltimes and scale and scaleN are integers. The function scales an absolute time interval [start,end] according to the triplets. Each triplet defines an interval of the day and a scale factor. If there is any time interval of the day that is not covered by the triplets, that time is scaled by the scale factor.
>
> |  |  |
> | --- | --- |
> | Example 1 | %X% = scale\_time(%start%,%end%,0,22:00,06:00,3);  The variable%X% will be the number of night time hours (22:00-06:00) within the interval [%start%,%end%] multiplied by 3. Note that if the interval [%start%,%end%] covers many days, each night period will be scaled and added to the result. |
>
> |  |  |
> | --- | --- |
> | Example 2 | %Y% = scale\_time(%start%,%end%,1, 22:00,02:00,2, 02:00,06:00,4); |
>
> add\_weeks(abstime,weeks)  
> add\_months(abstime,months)  
> add\_years(abstime,years)
>
> Returns the given absolute time plus a number of weeks/months/years. The second argument must be an integer.
>
> The date is rounded up if the requested date does not exist, for example, adding 1 month to January 31 will result in March 1. And adding 1 year to the leap day February 29, 2004 will also result in March 1.
>
> round\_down(value,step)  
> round\_up(value,step)
>
> Returns the given value (integer, reltime or abstime) rounded up/down the nearest multiple of the given step (integer or reltime).
>
> For absolute times, an integral number of steps from 1 Jan 1986 00:00 will be found. This matters only when rounding up to a step which is not a whole day, nor an integral fraction thereof.
>
> round\_down\_week(abstime)  
> round\_up\_week(abstime)
>
> Returns the given absolute time rounded down or up to the nearest beginning of a week.
>
> round\_down\_month(abstime)  
> round\_up\_month(abstime)
>
> Returns the given absolute time rounded down or up to the nearest beginning of a month.
>
> round\_down\_year(abstime)  
> round\_up\_year(abstime)
>
> Returns the given absolute time rounded down or up to the nearest beginning of a year.
>
> round\_down\_offset(value,limit,offset)   
> round\_up\_offset(value,limit,offset)
>
> These functions are similar toround\_down and round\_up, but take an additional offset into account. They first subtract the offset from the value, round it to the given limit and finally add the offset. This is useful for rounding to a certain time in another time zone.
>
> time\_of\_day(abstime)
>
> Returns the relative time since midnight (the range is 0:00 to 23:59) of a given absolute time.
>
> time\_of\_week(abstime)
>
> Returns the relative time since the beginning of the week (the range is 0:00 to 167:59) of a given absolute time.
>
> time
>
> Returns the local absolute time. This function is mainly used in reports.
>
> Rule functions
>
> total\_rule\_penalty
>
> Returns the sum of all rule penalties on the current chain, or zero if no penalty is incurred. If a rule fails, the function still returns a value.
>
> rulefailure
>
> Returnstrue if any rule fails for the current chain, otherwise it returns false.
>
> rule\_failure(name)
>
> Returnstrue if the specified rule fails for the current object, for example the current duty if it is a duty rule.
>
> rule\_on(rule\_name)
>
> Returns the status of the rule on/off switch.true if the rule is turned on. Also applies to constraints.
>
> current\_rule\_id
>
> Returns the name of the rule currently being evaluated. This is often used for rule exceptions, when a specific rule should be ignored under certain conditions.
>
> current\_rule\_id will evaluate to void if it is not calculated from within a rule expression.
>
> Format functions
>
> Format functions are used together with Rave Publisher PDL, and allow an argument to be formatted into a string representation.
>
> format\_time(time,string[,locale])
>
> Allows a time or a date to be presented as a character string in a flexible way, with provisions made for multiple locales (languages). The function returns a formatted string.
>
> The first argument is the time that is to be formatted, and can be an abstime or a reltime. The second argument is a format string containing conversion codes that specify how different parts of the time parameter are to be converted into characters. The third argument, which is optional, specifies the locale used in the conversion.
>
> The conversion specifications in the format string look as follows:%[flags][width]conversion\_character.
>
> The available conversion characters are:
>
> |  |  |
> | --- | --- |
> | y | year, 0-99 |
> | Y | full year |
> | m | month, 1-12 |
> | d | date, 1-31 |
> | j | day, 1-366 |
> | H | hour, 0-23 |
> | I | hour, 1-12 |
> | h | hour, unlimited |
> | p | AM or PM |
> | M | minute, 0-59 |
> | w | weekday, 1-7 |
> | W | week number, 1-52 |
> | a | abbreviated weekday, for example Mon, Tue, Wed |
> | A | full weekday, for example Monday, Tuesday, Wednesday |
> | b | abbreviated month, for example Jan, Feb, Mar |
> | B | full month, for example January, February, March |
> | % | percent |
> | n | new line |
> | t | tab |
>
> The width section of the conversion specification is a number that controls the minimum number of characters generated. If the number of characters in the output of the associated conversion specification is less than the specified width, blanks or zeros are added.
>
> For reltimes, only the following conversion characters apply:h, M, %, n, and t. The behaviour is undefined with other characters.
>
> There are four flags that may be used in the conversion specification:
>
> |  |  |
> | --- | --- |
> | - | Output is left justified within its field. |
> | 0 | Leading zeros are used to pad the field when the converted output do not fill up the field width. |
> | u | Convert to uppercase. |
> | l | Convert to lowercase. |
>
> The last argument offormat\_time is optional and defines the locale to be used for names of weekdays, months, etc. Any locale supported by the host operating system (as shown for example with “locale -a”) is allowed. In special cases, the empty string ("") uses the locale defined by the environment. If the locale is omitted, English names are used.
>
> |  |  |
> | --- | --- |
> | Example 1 | format\_time(May 5 1994 15:40,     "Test: %Y-%02m-%02d %j %H:%02M %W %a %B %h","sv");  The output from this call toformat\_time is the string Test: 1994-05-05 125 15:40 18 Tor Maj 73119 |
>
> For backward compatibility, the locale argument can also be one of the following strings:
>
> |  |  |
> | --- | --- |
> | "G" | English |
> | "D" | German, using HP roman 8 encoding |
> | "SE" | Swedish, using HP roman 8 encoding |
> | "I" | Italian |
> | "NL" | Dutch |
>
> format\_int(int, format string)
>
> This function allows an integer to be formatted as a string in a flexible way. The first argument is the integer that is to be formatted into a string. The second argument is the format string that specifies how the integer should be formatted.
>
> The conversion specifications in the format string look as follows:%[prefix][width][thousand separator][decimal separator]{d|i}
>
> Theprefix] section can be any number of the following symbols:
>
> |  |  |
> | --- | --- |
> | - | Output is left justified within its field. Not compatible with the zero prefix. |
> | + | Output should always begin with a plus or minus sign. |
> | Blank | Same as plus, but begins with a blank instead of a plus for non-negative values. |
> | 0 | Use leading zeroes to pad the field. |
>
> The optional[width] specifies the minimum number of characters to be printed, including the sign and separator characters. Blank characters are inserted until the minimum length is obtained. If [width] is followed by a full stop (.) and a second number, the second number will be the minimum number of characters to be printed, not counting the sign character. Zeros are added until the minimum length is obtained.
>
> The[thousand separator] has the form wnwcw. It inserts the separators cw between every nw:th digit and the following digit, counting from the end or the digit left of the decimal separator nw=1..3..9, cw=separator character (not a digit).
>
> The[decimal separator], vnvcv, inserts the separator cv before the nv:th digit, by counting from the end nv=1..2..9, cv=separator character (not a digit).
>
> The last character in a conversion specification is either the characterd or i. They mean the same thing and refer to the integer value.
>
> The substring%% will result in one printed percent character.
>
> |  |  |
> | --- | --- |
> | Example 2 | format\_int(123, "x=%4d") -> "x= 123 format\_int(123, "x=%-4d") -> "x=123 " format\_int(123, "x=%+04d") -> "x=+123" format\_int(123, "x=%04d") -> "x=0123" format\_int(123, "x=%+v2.d") -> "x=+1.23" format\_int(123, "x=%08w3’v2:d") -> "x=0’001:23" format\_int(123, "x=%d %% y<>%+i") -> "x=123 % y<>+123" format\_int(-123, "x=%4d") -> "x=-123" |
>
> String functions
>
> locate(pattern,text[,start])
>
> The function returns the first position intext where the substring pattern occurs. If pattern does not occur in text, 0 is returned. start is an optional start position.
>
> |  |  |
> | --- | --- |
> | Example 1 | locate("men","Carmen") -> 4 |
>
> substr(s, start, length)
>
> Returns a part of the strings. start is the start position and length is the number of characters. If the start parameter is out of range, an empty string is returned.
>
> |  |  |
> | --- | --- |
> | Example 2 | substr("abcdefg", 3, 2) -> "cd" |
>
> length(s)
>
> Returns the number of characters in a string.
>
> |  |  |
> | --- | --- |
> | Example 3 | length("abc") -> 3 |
>
> concat(s1, s2, ..., sn)
>
> Returns a merged string of two or more smaller strings.
>
> The concatenated string will be truncated if the result is longer than 4095 characters.
>
> |  |  |
> | --- | --- |
> | Example 4 | concat("Carmen"," ","Systems")->"Carmen Systems" |
>
> msgr(s|concat(s1, s2, ..., sn))
>
> This function accepts a string or theconcat function as argument, and returns a translated string. The argument is translated via lookup in a gettext MO-file.
>
> Any constant string in the Rave code can be made translatable withmsgr. The special case with concat as argument is typically used for failtexts, which usually are constructed from concatenated strings.
>
> msgx(s)
>
> This function accepts a string as argument, and returns the string unchanged. The purpose of this function is to mark strings as candidates for translation when the actual translation (gettext lookup) is performed by another component than Rave itself.
>
> string\_to\_int(s)
>
> This function converts the string argument to an integer. For example, this can be useful when you need to sort strings numerically.
>
> A valid argument must have the following format:
>
> Zero or more white-space characters, followed by an optional+ or - character, followed by one or more digits, followed by zero or more white-space characters.
>
> When the argument cannot be converted to an integer, void is returned resulting in a run-time error.
>
> |  |  |
> | --- | --- |
> | Example 5 | string\_to\_int("0000000") is 0 (ignore non-significant 0 characters) string\_to\_int("0") is 0 string\_to\_int("589000000") is 589000000 string\_to\_int("-498780") is -498780 string\_to\_int("2147483648") is VOID (larger than 2^31 - 1) string\_to\_int("2147483647") is 2147483467 (2^31 - 1) string\_to\_int("-2147483647") is -2147483647 (-2^31 + 1) string\_to\_int("-2147483648") is VOID (-2^31 is a reserved value) string\_to\_int("+354") is 354 (ignore leading '+') string\_to\_int("12Xcv") is VOID string\_to\_int("") is VOID string\_to\_int(void\_string) is VOID string\_to\_int(" 34 56 ") is VOID string\_to\_int(" 3456 ") is 3456 (ignore leading and trailing spaces) |
>
> Void functions
>
> void(expr)
>
> Returnstrue if expr is void, otherwise false.
>
> default (expr1,expr2)
>
> Returnsexpr1 if it is not void. If expr1 is void, the function returns expr2.
>
> void(data\_type)
>
> Returns a void value of the given type.
>
> void\_bool
>
> Returns a void value of the typebool, can also be written void(bool).
>
> void\_int
>
> Returns a void value of the typeint, can also be written void(int).
>
> void\_abstime
>
> Returns a void value of the typeabstime, can also be written void(abstime).
>
> void\_reltime
>
> Returns a void value of the typereltime, can also be written void(reltime).
>
> void\_string
>
> Returns a void value of the typestring, can also be written void(string).
>
> Iterator functions
>
> index[(N)]
>
> Used together with Rave Publisher. Returns the index number of a loop construction in the report language.
>
> index and index(0) return the index number from the innermost currently active loop. index(1) returns the index number from the second innermost loop construction currently active in the report and so on for higher arguments.
>
> times\_index(N)
>
> Used together with the special built-intimes iterator, to get the current count. The argument has the same meaning as for index, but refers to used times iterators instead of report loops.
>
> interval\_start
>
> Used together with the special built-in interval iterator, to get the current interval start.
>
> interval\_end
>
> Used together with the special built-in interval iterator, to get the current interval end.
>
> CAPI functions
>
> Rave has built-in support for external alertness prediction models that conform to the Common Alertness Prediction Interface (CAPI). Results from CAPI calculations are available via the following functions:
>
> capi\_legs
>
> Returns one prediction value per leg.
>
> capi\_time(abstime)
>
> Returns one prediction value for each chain and point in time.
>
> |  |  |
> | --- | --- |
> | Note | Definitions related to CAPI must reside in a Rave rule set module calledcapi. |
>
> For more information see,[API reference,](../../apidoc/rave.sphinx/index.html) the capi\_test() method in the Rave Python API (available on Bag objects).

|  |  |
| --- | --- |
| [Rave Reference](index.html)  » | [previous](Expressions.05.12.html)  | [next](Expressions.05.14.html) |

|  |  |
| --- | --- |
| Rave Reference  Component version 1.0.16  Jeppesen Proprietary |  |