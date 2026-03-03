## Functions

### carmensystems.publisher.api.Font


`carmensystems.publisher.api.``Font`(*face=None*, *size=None*, *weight=None*, *style=None*)
:   Synonym for [`font()`](carmensystems.publisher.api.font.html#carmensystems.publisher.api.font "carmensystems.publisher.api.font").

### carmensystems.publisher.api.action


`carmensystems.publisher.api.``action`(*function*, *args=()*)
:   Creates an action for a component. When the component is clicked,
    **function** is invoked with arguments **args** .

    |  |  |
    | --- | --- |
    | Parameters: | * **function** (`function`) – function to be invoked. * **args** (`tuple` or `list`) – arguments to use in invocation. |

### carmensystems.publisher.api.bookmark


`carmensystems.publisher.api.``bookmark`(*text*, *level=1*, *open=True*)
:   PDF only: create a bookmark for a component.

    Use as value for keyword argument **bookmark** in constructors
    and `set()` methods.

    |  |  |
    | --- | --- |
    | Parameters: | * **text** (`string`) – the text shown in the bookmark list. * **level** (`int`) – the level of nesting. Level 1 is a top-level bookmark;   bookmark with higher level will be shown nested in the   previous bookmark with a lower level. * **open** (`bool`) – whether or not the bookmark should be expanded in   the bookmark view. |

### carmensystems.publisher.api.border


`carmensystems.publisher.api.``border`(*left=None*, *top=None*, *right=None*, *bottom=None*, *inner\_floor=None*, *inner\_wall=None*, *colour='#000000'*)
:   Create a border around a component’s cell area, and optionally between nested components.

    Use as value for keyword argument **border** in constructors
    and `set()` methods.

    |  |  |
    | --- | --- |
    | Parameters: | * **colour** (*colour constant*) – border colour * **left** (*int* or *float*) – Thickness of the left part of the border * **top** (*int* or *float*) – Thickness of the top part of the border * **right** (*int* or *float*) – Thickness of the right part of the border * **bottom** (*int* or *float*) – Thickness of the bottom part of the border * **inner\_floor** (*int* or *float*) – Thickness of horizontal borders between components * **inner\_wall** (*int* or *float*) – Thickness of vertical borders between components |

### carmensystems.publisher.api.border_all


`carmensystems.publisher.api.``border_all`(*w=1*, *colour='#000000'*)
:   Shorthand for :obj:`` `border ``<border>```(left=w, top=w, right=w, bottom=w, inner\_floor=w, inner\_wall=w, colour=colour)``.

### carmensystems.publisher.api.border_frame


`carmensystems.publisher.api.``border_frame`(*w=1*, *colour='#000000'*)
:   Shorthand for :obj:`` `border ``<border>```(left=w, top=w, right=w, bottom=w, colour=colour)``

### carmensystems.publisher.api.chartaction


`carmensystems.publisher.api.``chartaction`(*fun*)
:   Creates an action for a graphic object in a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart"), e.g. a bar or
    a marker. When the object is clicked, **function** is invoked. It is
    always passed two arguments: The coordinates that the object
    represents in the chart.

    Use as value for keyword argument **action** in the [`Series`](carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series")
    constructor.

    |  |  |
    | --- | --- |
    | Parameters: | **function** (`function`) – function to be invoked. |

### carmensystems.publisher.api.chartlink


`carmensystems.publisher.api.``chartlink`(*module*, *params={}*, *context=None*)
:   Create a link from a graphic object in a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") to another
    Publisher report.

    Use as value for keyword argument **link** in the [`Series`](carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series") constructor.

    |  |  |
    | --- | --- |
    | Parameters: | * **module** (`string` or `function`) – Either the module name of the other report, or   a function from chart coordinates to module name. * **params** (`dict {string : string`} or `function`) – parameters to be passed to the other report   (available via the [`Report.arg()`](carmensystems.publisher.api.Report.html#carmensystems.publisher.api.Report.arg "carmensystems.publisher.api.Report.arg") method).   May also be a function from chart coordinates   to parameters. * **context** (*application buffer* *or* *context locator*) – Specifies the context in which the other report   is to be generated. |

### carmensystems.publisher.api.charttooltip


`carmensystems.publisher.api.``charttooltip`(*fun*)
:   Creates a tooltip for a graphic object in a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart"), e.g. a bar or
    a marker.

    Use as value for keyword argument **tooltip** in the [`Series`](carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series")
    constructor.

    |  |  |
    | --- | --- |
    | Parameters: | **fun** (`function`) – Function from chart coordinates to tooltip string. Function arguments are the x and y coordinates. |

### carmensystems.publisher.api.charturl


`carmensystems.publisher.api.``charturl`(*url*, *params={}*)
:   Create a link from a graphic object in a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") to a webpage.

    Use as value for keyword argument **link** in the [`Series`](carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series") constructor.

    |  |  |
    | --- | --- |
    | Parameters: | * **url** (`string` or `function`) – Either a URL, or a function from chart coordinates   to a URL. * **params** (`dict {string : string`} or `function`) – parameters to be passed as part of the URL.   May also be a function from chart coordinates   to parameters. |

### carmensystems.publisher.api.errmsg


`carmensystems.publisher.api.``errmsg`(*source*, *err*)
:   Format error message with a message consisting of report name,
    exception text and stack trace.
    Stack trace is generated only if the report exception is the last
    issued exception.

    |  |  |
    | --- | --- |
    | Parameters: | * **source** (*string*) – the module name of the report * **err** (*Exception*) – exception generated from report generation |
    | Returns: | formatted error message tuple (logerr, htmlerr) |
    | Return type: | (string, string) |

### carmensystems.publisher.api.font

### carmensystems.publisher.api.generateReport


`carmensystems.publisher.api.``generateReport`(*source*, *outputfile*, *format=1*, *reportparams={}*, *context=None*)
:   Render a report in the specified format and save it in **outputfile** .

    |  |  |
    | --- | --- |
    | Parameters: | * **source** (*string*) – the module name of the report * **outputfile** (*string*) – path to destination file.   If missing, extension is added according   to format (.pdf or .html)   Any additional files, such as image files for html,   are stored in the directory **outputfile** \_files. * **format** – either `PDF`, `HTML`, `CSV` or `TXT`; only use these   pre-defined module constants. **Default value:** PDF.   **Note:** I{Information may be lost when generating as text.   Only top-level text strings will appear in the output.} * **reportparams** (`dict`, where keys and values are `string`s) – Additional parameters to the report, passed   as a `dict` mapping parameter names to values.   In the report, the values can be retrieved   via the [`Report.arg()`](carmensystems.publisher.api.Report.html#carmensystems.publisher.api.Report.arg "carmensystems.publisher.api.Report.arg") method.   **Default value:** An empty dict. * **context** (*application buffer* *or* *context locator*) – context object to use in the report.   **Default value:** None. |
    | Returns: | the full path to the generated file |
    | Return type: | string |

### carmensystems.publisher.api.get_supported_report_class


`carmensystems.publisher.api.``get_supported_report_class`(*module\_name*)
:   Return the class of the report.
    Deprecated 2016-01-18: Get report metadata from the module instead of from the report class.

    |  |  |
    | --- | --- |
    | Parameters: | **module\_name** (*string*) – name of the python module including the report |
    | Returns: | The report class if it exists |
    | Return type: | [type](https://docs.python.org/2.7/library/functions.html#type "(in Python v2.7)") |

### carmensystems.publisher.api.javascriptAction


`carmensystems.publisher.api.``javascriptAction`(*function*)
:   Creates a javascript action for a component. When the component is clicked,
    **function** is invoked.

    |  |  |
    | --- | --- |
    | Parameters: | **function** (`string`) – function to be invoked in the form ‘functionName(arg1, arg2, …)’. |

### carmensystems.publisher.api.link


`carmensystems.publisher.api.``link`(*module*, *params={}*, *context=None*)
:   Create a link from a component to another Publisher report.

    Use as value for keyword argument **link** in constructors
    and methods.

    |  |  |
    | --- | --- |
    | Parameters: | * **module** (`string`) – the module name of the other report. * **params** (`dict {string : string`}) – parameters to be passed to the other report   (available via the [`Report.arg()`](carmensystems.publisher.api.Report.html#carmensystems.publisher.api.Report.arg "carmensystems.publisher.api.Report.arg") method). * **context** (*application buffer* *or* *context locator*) – Specifies the context in which the other report   is to be generated. |

### carmensystems.publisher.api.padding


`carmensystems.publisher.api.``padding`(*left=None*, *top=None*, *right=None*, *bottom=None*)
:   Create padding (space between border and content) for a component.
    Also used to specify page margins.

    The returned object is a valid value for keyword argument **padding** in constructors and methods, and for keyword argument **margins** in [`Report.set()`](carmensystems.publisher.api.Report.html#carmensystems.publisher.api.Report.set "carmensystems.publisher.api.Report.set"). None, keep old/default value.

### carmensystems.publisher.api.render


`carmensystems.publisher.api.``render`(*report*, *format*)

### carmensystems.publisher.api.url


`carmensystems.publisher.api.``url`(*path*, *params={}*)
:   Create a link from a component to an internet page.

    Use as value for keyword argument **link** in constructors
    and methods.

    |  |  |
    | --- | --- |
    | Parameters: | * **path** (`string`) – the URL. * **params** (`dict {string : string`}) – parameters to be passed via the URL. |