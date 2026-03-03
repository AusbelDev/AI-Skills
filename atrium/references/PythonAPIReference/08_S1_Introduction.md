## Introduction


The [`jcms.basics.time`](jcms.basics.time.html#module-jcms.basics.time "jcms.basics.time") module contains functions for time computations. Many
functions are equivalent to built-in time functions in Rave. Examples:
[`add_weeks()`](jcms.basics.time.html#jcms.basics.time.add_weeks "jcms.basics.time.add_weeks"), [`round_down_month()`](jcms.basics.time.html#jcms.basics.time.round_down_month "jcms.basics.time.round_down_month"), and [`time_of_week()`](jcms.basics.time.html#jcms.basics.time.time_of_week "jcms.basics.time.time_of_week"). Other
functions are additions to what’s available in Rave. Examples: [`add_hours()`](jcms.basics.time.html#jcms.basics.time.add_hours "jcms.basics.time.add_hours") and
[`seconds_get_now()`](jcms.basics.time.html#jcms.basics.time.seconds_get_now "jcms.basics.time.seconds_get_now").

A typical use case for this module is to configure a report to use the data of the previous
calendar month.

#### Jeppesen time concepts

The *epoch* (the point where time starts) in Jeppesen products is 1986-01-01 00:00.
Compare with the Unix epoch which is 1970-01-01 00:00 (the Jeppesen epoch is 504921600
seconds after the Unix epoch).

`CarmTime` (`int` in Python) is the internal canonical representation of absolute
time. A point in time is represented as **the number of minutes** since the epoch. This
corresponds to the `abstime` datatype in Rave.

[`AbsTime`](../basics/abstime.html#AbsTime.AbsTime "AbsTime.AbsTime") is a class for absolute times. It can be constructed
from a `CarmTime` or from a string representation (the strings accepted by
[`AbsTime`](../basics/abstime.html#AbsTime.AbsTime "AbsTime.AbsTime") are not the same as the time strings below).

#### Time strings

The following string representations of points in time are supported by [`jcms.basics.time`](jcms.basics.time.html#module-jcms.basics.time "jcms.basics.time"):

* now
* YYYY-MM-DD
* YYYY-MM-DD HH:MM
* YYYY-MM-DD HH:MM:SS
* YYYY-MM-DD HH:MM:SS.SSS
* YYYY-MM-DDTHH:MM
* YYYY-MM-DDTHH:MM:SS
* YYYY-MM-DDTHH:MM:SS.SSS

#### Rave expression support

The [`minutes_from_expr()`](jcms.basics.time.html#jcms.basics.time.minutes_from_expr "jcms.basics.time.minutes_from_expr") and [`seconds_from_expr()`](jcms.basics.time.html#jcms.basics.time.seconds_from_expr "jcms.basics.time.seconds_from_expr") functions parse and evaluate expressions involving time functions in Rave. Syntax summary:

```
<expr> := now
        | YYYY-MM-DD
        | YYYY-MM-DD HH:MM
        | YYYY-MM-DD HH:MM:SS
        | YYYY-MM-DD HH:MM:SS.SSS
        | YYYY-MM-DDTHH:MM
        | YYYY-MM-DDTHH:MM:SS
        | YYYY-MM-DDTHH:MM:SS.SSS
        | <add>(<expr>, <int>)
        | <round>(<expr>)

<add>  := add_minutes
        | add_hours
        | add_days
        | add_weeks
        | add_months
        | add_years

<round> := round_down_minute | round_up_minute
         | round_down_hour   | round_up_hour
         | round_down_day    | round_up_day
         | round_down_week   | round_up_week
         | round_down_month  | round_up_month
         | round_down_year   | round_up_year
```

For more information about built-in functions in Rave, see the Rave documentation.

#### Examples

```
>>> import jcms.basics.time as T
>>> # Parameters: year, month, day, minutes
>>> t1 = T.encode_abstime(2011, 5, 26, 9*60+11)   # CarmTime
>>> t1, type(t1)
(13357991, <type 'int'>)
>>> T.time_of_day(t1)
551
>>> T.minutes_to_string(t1)
'2011-05-26 09:11'
>>> t2 = T.round_down_hour(t1)
>>> T.minutes_to_string(t2)
'2011-05-26 09:00'
>>> T.minutes_to_string(T.add_days(t2, 2))
'2011-05-28 09:00'
```

##### Using Rave expressions

Get the current time:

```
>>> now = T.minutes_from_expr("now")
>>> now      # doctest: +SKIP
13507635
>>> T.minutes_to_string(now)
'2011-09-07 07:17'
```

Define start and end dates for a one month period using Rave expressions, as follows:

```
>>> # The first day of the previous month
>>> start_date = "add_months(round_down_month(now), -1)"
>>> # The first day of the current month
>>> end_date = "round_down_month(now)"
```

```
>>> # Evaluate the expressions
>>> start = T.minutes_from_expr(start_date)
>>> end = T.minutes_from_expr(end_date)
```

```
>>> T.minutes_to_string(start)
'2011-08-01 00:00'
>>> T.minutes_to_string(end)
'2011-09-01 00:00'
```

### Jeppesen time concepts

### Time strings

### Rave expression support

### Examples

#### Using Rave expressions