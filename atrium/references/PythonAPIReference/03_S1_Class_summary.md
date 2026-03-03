## Class summary

### carmensystems.publisher.api.Area


*class* `carmensystems.publisher.api.``Area`(*fill=None*)
:   Shows [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as an area graph: like a [`Line`](carmensystems.publisher.api.Line.html#carmensystems.publisher.api.Line "carmensystems.publisher.api.Line") graph,
    except the area under the line is filled.

    Inheritance

    ![Inheritance diagram of Area](../../_images/inheritance-7018ed32bbd6eaca179aaf07ff05694f1ad57953.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Area.__init__ "carmensystems.publisher.api.Area.__init__")([fill]) | |  |  | | --- | --- | | param fill: | colour (*colour constant* ) or pattern ([`FillPattern`](carmensystems.publisher.api.FillPattern.html#carmensystems.publisher.api.FillPattern "carmensystems.publisher.api.FillPattern")) | |

    Member details

    `__init__`(*fill=None*)
    :   |  |  |
        | --- | --- |
        | Parameters: | **fill** – colour (*colour constant* ) or pattern ([`FillPattern`](carmensystems.publisher.api.FillPattern.html#carmensystems.publisher.api.FillPattern "carmensystems.publisher.api.FillPattern")) to use for filling the area. Unlike [`Bar`](carmensystems.publisher.api.Bar.html#carmensystems.publisher.api.Bar "carmensystems.publisher.api.Bar"), the argument cannot be a function, since the area is common to all data. |

### carmensystems.publisher.api.Bar


*class* `carmensystems.publisher.api.``Bar`(*fill=None*, *width=1.0*, *offset=None*)
:   Shows [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as bar graphs.

    Inheritance

    ![Inheritance diagram of Bar](../../_images/inheritance-5d3420e43805aebcf0a42e75418573f24b82473f.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Bar.__init__ "carmensystems.publisher.api.Bar.__init__")([fill, width, offset]) | |  |  | | --- | --- | | param fill: | colour (*colour constant* ) or pattern ([`FillPattern`](carmensystems.publisher.api.FillPattern.html#carmensystems.publisher.api.FillPattern "carmensystems.publisher.api.FillPattern")) | |

    Member details

    `__init__`(*fill=None*, *width=1.0*, *offset=None*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **fill** – colour (*colour constant* ) or pattern ([`FillPattern`](carmensystems.publisher.api.FillPattern.html#carmensystems.publisher.api.FillPattern "carmensystems.publisher.api.FillPattern"))   to use for filling bars. May also be a function   from the x and y values to a colour or pattern,   to have different colours/patterns depending on   values. * **width** (`float`) – width to use for each data item, in relation to the   available space. 1.0 is all available space. * **offset** (`float`) – positions the left side of the graph in relation   to the available space. You normally   use values in the range 0.0 (inclusive) to 1.0   (exclusive).   0.0 means the graph will be left-justified within   the available space, 1.0 will put it   just outside the available space.  By default, the graph will be centered in the   available space, i.e. the offset will be   0.5 - **width** /2. |

### carmensystems.publisher.api.Box


*class* `carmensystems.publisher.api.``Box`
:   Abstract base class for all report components. Cannot be constructed.

    Inheritance

    ![Inheritance diagram of Box](../../_images/inheritance-dbc5abea4ffe64e2cf9c68cc570d23bc531416b5.png)

    Methods

    |  |  |
    | --- | --- |
    | [`set`](#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set")(\*\*properties) | Set properties for a report component. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `set`(*\*\*properties*)
    :   Set properties for a report component. All common properties are documented in detail here, but all subclasses do not accept all properties; the respective set() methods list the keywords that can be used.

        |  |  |
        | --- | --- |
        | Raises: | **NotImplementedError** – redefined in all subclasses. |
        | Parameters: | * **width** (`int`) – the minimum width of the component’s object area.   Note that the cell area occupied by the component   may be greater than the object area,   depending on widths and heights of the components   it is aligned with. The **align** and **valign**   properties place the component within its cell   area. * **height** (`int`) – the minimum height of the component’s object area.   Note that the cell area occupied by the component   may be greater than the component itself,   depending on widths and heights of the components   it is aligned with. The **align** and **valign**   properties place the component within its cell   area. * **name** (`string`) – names the component, so it can be referenced   from other components. See [`Crossref`](carmensystems.publisher.api.Crossref.html#carmensystems.publisher.api.Crossref "carmensystems.publisher.api.Crossref"). * **border** – draws a border around the component’s cell area.   Borders are created using functions [`border()`](carmensystems.publisher.api.border.html#carmensystems.publisher.api.border "carmensystems.publisher.api.border"),   [`border_frame()`](carmensystems.publisher.api.border_frame.html#carmensystems.publisher.api.border_frame "carmensystems.publisher.api.border_frame") or [`border_all()`](carmensystems.publisher.api.border_all.html#carmensystems.publisher.api.border_all "carmensystems.publisher.api.border_all"). * **padding** – adds extra space between the component and the   cell area boundaries. Use function [`padding()`](carmensystems.publisher.api.padding.html#carmensystems.publisher.api.padding "carmensystems.publisher.api.padding") to   specify padding. * **align** – horizontal positioning of the component within   its cell area. Valid values are module constants   `LEFT`, `CENTER` and `RIGHT`.   Default is `LEFT`. * **valign** – vertical positioning of the component within   its cell area. Valid values are module constants   `TOP`, `CENTER` and `BOTTOM`.   Default is `TOP`. * **font** – font to use in component. Fonts are created with   function [`font()`](carmensystems.publisher.api.font.html#carmensystems.publisher.api.font "carmensystems.publisher.api.font"). * **colour** – foreground colour, i.e. colour of text and lines.   Colours are defined as colour constants: a   string on the form `'#RRGGBB'` specifying the RGB   value. (Tip: use a [`ColourPalette`](carmensystems.publisher.api.ColourPalette.html#carmensystems.publisher.api.ColourPalette "carmensystems.publisher.api.ColourPalette").) * **colspan** (`int`) – the number of columns that the component should   occupy, in relation to components in adjoining rows. * **rowspan** (`int`) – the number of rows that the component should occupy,   in relation to components in adjoining columns. * **background** – background colour of the component and its cell space.   Like **colour** , the value should be a   *colour constant* . (Tip: use a [`ColourPalette`](carmensystems.publisher.api.ColourPalette.html#carmensystems.publisher.api.ColourPalette "carmensystems.publisher.api.ColourPalette").) * **bookmark** – PDF only: create a bookmark for the component in   the PDF document. Use the [`bookmark()`](carmensystems.publisher.api.bookmark.html#carmensystems.publisher.api.bookmark "carmensystems.publisher.api.bookmark") function   to specify the bookmark. * **link** – HTML only: create a link from the component to   another report or webpage. Use functions [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url")or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link") to specify the link. * **action** – HTML only: create an action, i.e. a function   invocation, that will be triggered when clicking the   component. Use function [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action") to specify the   action. * **tooltip** – HTML only: tooltip shown when hovering over the component. |

### carmensystems.publisher.api.CSVReport


*class* `carmensystems.publisher.api.``CSVReport`(*outputfile=None*, *reportparams={}*, *context=None*)
:   Base class to use for creating CSV reports.

    **Note:** This is an Atrium-only feature (not supported in Studio).

    |  |  |
    | --- | --- |
    | Variables: | **data** – List with one sublist for each row |

    Inheritance

    ![Inheritance diagram of CSVReport](../../_images/inheritance-23b2534f89c9c25016285799d3f81c208d807ed5.png)



    Methods

    |  |  |
    | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.CSVReport.__init__ "carmensystems.publisher.api.CSVReport.__init__")([outputfile, reportparams, context]) | Initialize self. |
    | [`arg`](#carmensystems.publisher.api.CSVReport.arg "carmensystems.publisher.api.CSVReport.arg")(paramname) | |  |  | | --- | --- | | param paramname: | The name of the parameter passed to the report. | |
    | [`create`](#carmensystems.publisher.api.CSVReport.create "carmensystems.publisher.api.CSVReport.create")() | Abstract method supposed to populate the `data` instance attribute. |
    | [`run`](#carmensystems.publisher.api.CSVReport.run "carmensystems.publisher.api.CSVReport.run")() | The method used to generate the report. |

    Member details

    `__init__`(*outputfile=None*, *reportparams={}*, *context=None*)
    :   Initialize self. See help(type(self)) for accurate signature.

    `arg`(*paramname*)
    :   |  |  |
        | --- | --- |
        | Parameters: | **paramname** (*string*) – The name of the parameter passed to the report. |
        | Returns: | the parameter value, or None if no such parameter has been passed to the report. |
        | Return type: | [object](https://docs.python.org/2.7/library/functions.html#object "(in Python v2.7)") |

    `create`()
    :   Abstract method supposed to populate the `data` instance attribute. Must be redefined in subclasses.

    `run`()
    :   The method used to generate the report.
        Calls the report’s `create` method.

### carmensystems.publisher.api.Canvas


*class* `carmensystems.publisher.api.``Canvas`(*self*, *width*, *height*, *\*\*properties*)
:   A user-defined drawing. Subclass this and redefine the `draw()`method. If your subclass has a constructor, make sure it calls
    the Canvas constructor.

    |  |  |
    | --- | --- |
    | Parameters: | * **width** (`int`) – the width of the canvas * **height** (`int`) – the height of the canvas * **properties** – keyword arguments listed in [`set`](carmensystems.publisher.api.Text.html#carmensystems.publisher.api.Text.set "carmensystems.publisher.api.Text.set") can be used. |

    Inheritance

    ![Inheritance diagram of Canvas](../../_images/inheritance-93b1dcf7e6c0229fffbb0be2acdeba7ef9515c00.png)

    Methods

    |  |  |
    | --- | --- |
    | [`draw`](#carmensystems.publisher.api.Canvas.draw "carmensystems.publisher.api.Canvas.draw")(gc) | This is where all drawing is done, using the graphic **gc** . |
    | [`set`](#carmensystems.publisher.api.Canvas.set "carmensystems.publisher.api.Canvas.set")(self[, name, border, padding, align, …]) | Set component properties. |
    | [`size`](#carmensystems.publisher.api.Canvas.size "carmensystems.publisher.api.Canvas.size")(self) | The size of this Canvas; width and height values given to the constructor. |

    Attributes

    |  |  |
    | --- | --- |
    | `p_font` |  |
    | `p_foreground` |  |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `draw`(*gc*)
    :   This is where all drawing is done, using the graphic **gc** .
        It is called automatically during report generation, and must not be called by the user.

        Note that this method may be called several times during report generation, so avoid performance-heavy operations.

        |  |  |
        | --- | --- |
        | Raises: | **NotImplementedError** – always. Has to be redefined in subclasses. |
        | Parameters: | **gc** ([`Graphic`](carmensystems.publisher.api.Graphic.html#carmensystems.publisher.api.Graphic "carmensystems.publisher.api.Graphic")) – A [`graphic`](carmensystems.publisher.api.Graphic.html#carmensystems.publisher.api.Graphic "carmensystems.publisher.api.Graphic") object to use for drawing. |

    `set`(*self*, *name=None*, *border=None*, *padding=None*, *align=None*, *valign=None*, *font=None*, *colour=None*, *colspan=None*, *rowspan=None*, *background=None*, *bookmark=None*, *link=None*, *action=None*, *tooltip=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **name** – * **border** – * **padding** – * **align** – * **valign** – * **font** – default font for the Canvas * **colour** – default foreground colur for the Canvas * **colspan** – * **rowspan** – * **background** – * **bookmark** – * **link** – * **action** – * **tooltip** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

    `size`(*self*)
    :   The size of this Canvas; width and height values given to the
        constructor.

        |  |  |
        | --- | --- |
        | Returns: | a (width, height) tuple |

### carmensystems.publisher.api.Chart


*class* `carmensystems.publisher.api.``Chart`(*width*, *height*, *\*layers*, *\*\*properties*)
:   A graphic chart: show values in a coordinate system
    using bar graphs, line graphs etc.

    A Chart can display one or more layers of data, where each layer
    represents a set of (x,y) value pairs. All layers share a
    common x-axis, but have separate y-axes.

    Inheritance

    ![Inheritance diagram of Chart](../../_images/inheritance-2a92b7f1d0190b01598c48a0d187b4987476ca4f.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Chart.__init__ "carmensystems.publisher.api.Chart.__init__")(width, height, \*layers, \*\*properties) | |  |  | | --- | --- | | param width: | the width of the chart | |
    | [`draw`](#carmensystems.publisher.api.Chart.draw "carmensystems.publisher.api.Chart.draw")(gc) | Called automatically; do not use. |
    | [`set`](#carmensystems.publisher.api.Chart.set "carmensystems.publisher.api.Chart.set")(self[, name, border, padding, align, …]) | Set component properties. |
    | [`size`](#carmensystems.publisher.api.Chart.size "carmensystems.publisher.api.Chart.size")(self) | The size of this Canvas; width and height values given to the constructor. |

    Attributes

    |  |  |
    | --- | --- |
    | `p_font` |  |
    | `p_foreground` |  |

    Member details

    `__init__`(*width*, *height*, *\*layers*, *\*\*properties*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **width** (`int`) – the width of the chart * **height** (`int`) – the height of the chart * **layers** – one or more layers of data to present in this   Chart. Layers are either [`Series`](carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series") or [`Combine`](carmensystems.publisher.api.Combine.html#carmensystems.publisher.api.Combine "carmensystems.publisher.api.Combine")s.   x-axis values from different layers must have   matching types. * **xaxis\_name** (`string`) – x-axis label. * **xaxis\_limits** (`tuple`) – a (min,max) tuple specifying min and max   values for the x-axis. To set only min or   only max, set the other value to `None`.   The limits may be pushed to include all values,   and to fit the placing of the tick marks. * **xaxis\_format** (`function`) – formatting function to use when writing   values on the tick marks. Should take an   x value and return a `string` * **xaxis\_rotate\_tags** (`bool`) – whether to rotate the tags on the   x-axis by 90 degrees   counter-clockwise (default False).   Multi-line tags are not supported in   combination with rotated tags. * **border** – * **padding** – * **align** – * **valign** – * **colspan** – * **rowspan** – * **bookmark** – * **background** – background colour of the canvas *and* its cell   area. * **colour** – default foreground colour (for text and lines) * **font** – font used in the chart. * **name** – * **link** – * **action** – * **tooltip** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

    `draw`(*gc*)
    :   Called automatically; do not use.

    `set`(*self*, *name=None*, *border=None*, *padding=None*, *align=None*, *valign=None*, *font=None*, *colour=None*, *colspan=None*, *rowspan=None*, *background=None*, *bookmark=None*, *link=None*, *action=None*, *tooltip=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **name** – * **border** – * **padding** – * **align** – * **valign** – * **font** – default font for the Canvas * **colour** – default foreground colur for the Canvas * **colspan** – * **rowspan** – * **background** – * **bookmark** – * **link** – * **action** – * **tooltip** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

    `size`(*self*)
    :   The size of this Canvas; width and height values given to the
        constructor.

        |  |  |
        | --- | --- |
        | Returns: | a (width, height) tuple |

### carmensystems.publisher.api.ColourPalette


*class* `carmensystems.publisher.api.``ColourPalette`(*\*\*colourmap*)
:   Define a colour palette for use in a Report.
    All attributes are *colour constant* s. Available attributes are
    `Black` and `White`, plus all keyword arguments given to the constructor.

    Inheritance

    ![Inheritance diagram of ColourPalette](../../_images/inheritance-60f2e704fd97ffdae85d6764e2c363bb50a0a7dd.png)



    Methods

    |  |  |
    | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.ColourPalette.__init__ "carmensystems.publisher.api.ColourPalette.__init__")(\*\*colourmap) | All keyword arguments become attributes of the ColourPalette. |

    Member details

    `__init__`(*\*\*colourmap*)
    :   All keyword arguments become attributes of the ColourPalette. Values
        are assumed to be *colour constant* s.

        Examples:

        ```
        c = ColourPalette()
        # attributes: c.Black and c.White

        c = ColourPalette(Red='#ff3333', Green='#33ff60', Yellow='#ffffcc')
        # attributes: c.Black, c.White, c.Red, c.Green, c.Yellow

        colourmap = {'Blue':'#3300ff', 'Purple':'#990099'}
        c = ColourPalette(**colourmap)
        # attributes: c.Black, c.White, c.Blue, c.Purple
        ```

### carmensystems.publisher.api.Column


*class* `carmensystems.publisher.api.``Column`(*self*, *\*components*, *\*\*properties*)
:   Components laid out vertically.

    |  |  |
    | --- | --- |
    | Parameters: | * **components** – components of the column. More components can   be added with the [`add()`](#carmensystems.publisher.api.Column.add "carmensystems.publisher.api.Column.add") method. * **properties** – keyword arguments listed in [`set`](#carmensystems.publisher.api.Column.set "carmensystems.publisher.api.Column.set")can be used. |

    Inheritance

    ![Inheritance diagram of Column](../../_images/inheritance-7ff2765713cda6af05f33273ecd59152df80688f.png)

    Methods

    |  |  |
    | --- | --- |
    | [`add`](#carmensystems.publisher.api.Column.add "carmensystems.publisher.api.Column.add")(self, box) | Add **box** to the end of this Column, below any previously added boxes. |
    | [`add_footer`](#carmensystems.publisher.api.Column.add_footer "carmensystems.publisher.api.Column.add_footer")(self, box[, column]) | |  |  | | --- | --- | | param box: | the component to use as footer; any Box. | |
    | [`add_header`](#carmensystems.publisher.api.Column.add_header "carmensystems.publisher.api.Column.add_header")(self, box[, column]) | |  |  | | --- | --- | | param box: | the component to use as header; any Box. | |
    | [`newpage`](#carmensystems.publisher.api.Column.newpage "carmensystems.publisher.api.Column.newpage")(self) | Hard page break: Always add a page break at this place in the column. |
    | [`page`](#carmensystems.publisher.api.Column.page "carmensystems.publisher.api.Column.page")(self) | Soft page break, high priority: Add a page break at this place in the column if all content up to the next [`newpage()`](#carmensystems.publisher.api.Column.newpage "carmensystems.publisher.api.Column.newpage") or page() will not fit into the current page. |
    | [`page0`](#carmensystems.publisher.api.Column.page0 "carmensystems.publisher.api.Column.page0")(self) | Soft page break, low priority: Add a page break at this place in the column if all content up to the next page break – of any priority – will not fit into the current page. |
    | [`set`](#carmensystems.publisher.api.Column.set "carmensystems.publisher.api.Column.set")(self[, width, border, font, colour, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `add`(*self*, *box*)
    :   Add **box** to the end of this Column, below any previously added boxes.

    `add_footer`(*self*, *box*, *column=self*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **box** – the component to use as footer; any Box. * **column** – The column to which this footer belongs, default is self. |

    `add_header`(*self*, *box*, *column=self*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **box** – the component to use as header; any Box. * **column** – The column to which this header belongs, default is self. |

    `newpage`(*self*)
    :   Hard page break: Always add a page break at this place in the column.

    `page`(*self*)
    :   Soft page break, high priority: Add a page break at this place in the column if all content up to the next [`newpage()`](#carmensystems.publisher.api.Column.newpage "carmensystems.publisher.api.Column.newpage") or page() will not fit into the current page.

    `page0`(*self*)
    :   Soft page break, low priority: Add a page break at this place in the column if all content up to the next page break – of any priority – will not fit into the current page.

    `set`(*self*, *width=None*, *border=None*, *font=None*, *colour=None*, *colspan=None*, *background=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **width** – minimum width of the Column, even if the Column   is empty. **height** can not be set. * **border** – * **font** – default font for components in the Column. * **colour** – default foreground colour for components in   the Column. * **colspan** – minimum colspan of Column, even if it is empty.   **rowspan** can not be set. * **background** – default background colour for components in   the Column. |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.Combine


*class* `carmensystems.publisher.api.``Combine`(*\*layers*, *\*\*properties*)
:   Combine several layers of [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") data in the same coordinate system.
    Data layers in a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") always have the same x-axis, but layers
    in a Combine also share y-axis.
    Layers can be either [`Series`](carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series") or other `Combine`s

    Inheritance

    ![Inheritance diagram of Combine](../../_images/inheritance-3a0f23f281ac8c68b07f869f43f2e99b03f6d3f6.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Combine.__init__ "carmensystems.publisher.api.Combine.__init__")(\*layers, \*\*properties) | |  |  | | --- | --- | | param layers: | data layers to combine | |

    Member details

    `__init__`(*\*layers*, *\*\*properties*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **layers** – data layers to combine   ([`Series`](carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series") or other `Combine`s).   The type of the values must match between   layers, both on the x-axis and the y-axis. * **yaxis\_name** (`string`) – y-axis label. * **yaxis\_limits** (`tuple`) – a (min,max) tuple specifying min and max   values for the y-axis. To set only min or   only max, set the other value to `None`.   The limits may be pushed to include all values,   and to fit the placing of the tick marks. * **yaxis\_format** (`function`) – formatting function to use when writing   values on the tick marks. Should take a   y value and return a `string` * **on\_top** (`bool`) – if `True` (the default), y values from   different layers will be shown on top of   each other, so that the total y value is   the sum of the y values from all layers. |

### carmensystems.publisher.api.Container


*class* `carmensystems.publisher.api.``Container`
:   Abstract base class for boxes that align several other boxes

    Inheritance

    ![Inheritance diagram of Container](../../_images/inheritance-cc00b1b051f5bfd5addb0ed263107816a27a1923.png)

    Methods

    |  |  |
    | --- | --- |
    | [`add`](#carmensystems.publisher.api.Container.add "carmensystems.publisher.api.Container.add")(self, box) | Add **box** to this box |
    | [`set`](#carmensystems.publisher.api.Container.set "carmensystems.publisher.api.Container.set")(\*\*properties) | Set properties for a report component. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `add`(*self*, *box*)
    :   Add **box** to this box

    `set`(*\*\*properties*)
    :   Set properties for a report component. All common properties are documented in detail here, but all subclasses do not accept all properties; the respective set() methods list the keywords that can be used.

        |  |  |
        | --- | --- |
        | Raises: | **NotImplementedError** – redefined in all subclasses. |
        | Parameters: | * **width** (`int`) – the minimum width of the component’s object area.   Note that the cell area occupied by the component   may be greater than the object area,   depending on widths and heights of the components   it is aligned with. The **align** and **valign**   properties place the component within its cell   area. * **height** (`int`) – the minimum height of the component’s object area.   Note that the cell area occupied by the component   may be greater than the component itself,   depending on widths and heights of the components   it is aligned with. The **align** and **valign**   properties place the component within its cell   area. * **name** (`string`) – names the component, so it can be referenced   from other components. See [`Crossref`](carmensystems.publisher.api.Crossref.html#carmensystems.publisher.api.Crossref "carmensystems.publisher.api.Crossref"). * **border** – draws a border around the component’s cell area.   Borders are created using functions [`border()`](carmensystems.publisher.api.border.html#carmensystems.publisher.api.border "carmensystems.publisher.api.border"),   [`border_frame()`](carmensystems.publisher.api.border_frame.html#carmensystems.publisher.api.border_frame "carmensystems.publisher.api.border_frame") or [`border_all()`](carmensystems.publisher.api.border_all.html#carmensystems.publisher.api.border_all "carmensystems.publisher.api.border_all"). * **padding** – adds extra space between the component and the   cell area boundaries. Use function [`padding()`](carmensystems.publisher.api.padding.html#carmensystems.publisher.api.padding "carmensystems.publisher.api.padding") to   specify padding. * **align** – horizontal positioning of the component within   its cell area. Valid values are module constants   `LEFT`, `CENTER` and `RIGHT`.   Default is `LEFT`. * **valign** – vertical positioning of the component within   its cell area. Valid values are module constants   `TOP`, `CENTER` and `BOTTOM`.   Default is `TOP`. * **font** – font to use in component. Fonts are created with   function [`font()`](carmensystems.publisher.api.font.html#carmensystems.publisher.api.font "carmensystems.publisher.api.font"). * **colour** – foreground colour, i.e. colour of text and lines.   Colours are defined as colour constants: a   string on the form `'#RRGGBB'` specifying the RGB   value. (Tip: use a [`ColourPalette`](carmensystems.publisher.api.ColourPalette.html#carmensystems.publisher.api.ColourPalette "carmensystems.publisher.api.ColourPalette").) * **colspan** (`int`) – the number of columns that the component should   occupy, in relation to components in adjoining rows. * **rowspan** (`int`) – the number of rows that the component should occupy,   in relation to components in adjoining columns. * **background** – background colour of the component and its cell space.   Like **colour** , the value should be a   *colour constant* . (Tip: use a [`ColourPalette`](carmensystems.publisher.api.ColourPalette.html#carmensystems.publisher.api.ColourPalette "carmensystems.publisher.api.ColourPalette").) * **bookmark** – PDF only: create a bookmark for the component in   the PDF document. Use the [`bookmark()`](carmensystems.publisher.api.bookmark.html#carmensystems.publisher.api.bookmark "carmensystems.publisher.api.bookmark") function   to specify the bookmark. * **link** – HTML only: create a link from the component to   another report or webpage. Use functions [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url")or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link") to specify the link. * **action** – HTML only: create an action, i.e. a function   invocation, that will be triggered when clicking the   component. Use function [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action") to specify the   action. * **tooltip** – HTML only: tooltip shown when hovering over the component. |

### carmensystems.publisher.api.Crossref


*class* `carmensystems.publisher.api.``Crossref`(*self*, *name*, *size=None*, *format=None*)
:   Creates a cross reference or an internal link to a page number or to a named component elsewhere in the report. Used as part of the text in a [`Text`](carmensystems.publisher.api.Text.html#carmensystems.publisher.api.Text "carmensystems.publisher.api.Text") box. By default, this creates an internal link, where the link text contains the number of the page that the referred component appears on. When referring to one of the special names `'current_page'` or `'last_page'`, the result is just a page number being filled-in; no link is created.

    |  |  |
    | --- | --- |
    | Parameters: | * **name** – name of the referred component, as set by the [`name`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") property, or one of:    + `'current_page'`: resolves to the number of the current page   + `'last_page'`: resolves to the number of the last page * **format** – A format string, in the normal python syntax, containing   a format specifier for the page number (an integer).   This is the text that will appear in the report.   It is important to set the field width of the specifier   to the maximum number of digits in the page number, or   the layout might break.   The specifier may also be left out, to have a link text   without a page number.   **Default value** : `'%3i'`. |

    Inheritance

    ![Inheritance diagram of Crossref](../../_images/inheritance-ff4fcbac2603e0e7d69dc4ac01034c380fb1e3fc.png)

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

### carmensystems.publisher.api.Expandable


*class* `carmensystems.publisher.api.``Expandable`(*self*, *header*, *body*, *\*\*properties*)
:   In interactive output, creates a control (header) which lets the user control the visibility of an expandable section (body). In other outputs, the header text becomes a regular heading for the always visible body.

    |  |  |
    | --- | --- |
    | Parameters: | * **header** – clickable item to control visibility of the   body; Must be a [`Text`](carmensystems.publisher.api.Text.html#carmensystems.publisher.api.Text "carmensystems.publisher.api.Text") box or a string. * **body** – the component to expand; any [`Box`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box "carmensystems.publisher.api.Box"). * **properties** – keyword arguments listed in [`set`](#carmensystems.publisher.api.Expandable.set "carmensystems.publisher.api.Expandable.set")can be used. |

    Inheritance

    ![Inheritance diagram of Expandable](../../_images/inheritance-d1ea3a2e1cb2ac13178dfa8a6aa0f8915c1b30e3.png)

    Methods

    |  |  |
    | --- | --- |
    | [`set`](#carmensystems.publisher.api.Expandable.set "carmensystems.publisher.api.Expandable.set")(self[, width, border, font, colour, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `set`(*self*, *width=None*, *border=None*, *font=None*, *colour=None*, *colspan=None*, *background=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **width** – * **height** – * **border** – * **padding** – Padding for the expandable section (not the header),   default is left=8 for indentation. * **align** – * **valign** – * **font** – * **colour** – * **colspan** – * **rowspan** – * **background** – |

        See: [`Isolate.set()`](carmensystems.publisher.api.Isolate.html#carmensystems.publisher.api.Isolate.set "carmensystems.publisher.api.Isolate.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.FillPattern


*class* `carmensystems.publisher.api.``FillPattern`
:   Base class for patterns used to fill polygons in a [`Canvas`](carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas").

    Do not use; only instantiate subclasses

    Inheritance

    ![Inheritance diagram of FillPattern](../../_images/inheritance-2b4e51fcf0dcbef54c78617fc0157ed565ea87f6.png)

    Methods



    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

### carmensystems.publisher.api.Footer


*class* `carmensystems.publisher.api.``Footer`(*self*, *box*, *\*\*properties*)
:   A running footer for the report. Can only be added to the [`Report`](carmensystems.publisher.api.Report.html#carmensystems.publisher.api.Report "carmensystems.publisher.api.Report").
    The footer is active from the next page, or the current page if no output has been generated yet, and until another footer is added. The layout of the footer is independent of the rest of the page.

    |  |  |
    | --- | --- |
    | Parameters: | * **box** – the box defining the footer layout. * **properties** – keyword arguments listed in [`set`](#carmensystems.publisher.api.Footer.set "carmensystems.publisher.api.Footer.set")can be used. |

    Inheritance

    ![Inheritance diagram of Footer](../../_images/inheritance-202e7829bfee17805ca6483dc6f0e8958e7cea28.png)

    Methods

    |  |  |
    | --- | --- |
    | [`add`](#carmensystems.publisher.api.Footer.add "carmensystems.publisher.api.Footer.add")(self, box) | Add **box** to the end of this Header/Footer, below any previously added boxes. |
    | [`set`](#carmensystems.publisher.api.Footer.set "carmensystems.publisher.api.Footer.set")(self[, width, height, border, padding, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `add`(*self*, *box*)
    :   Add **box** to the end of this Header/Footer, below any previously added boxes.

    `set`(*self*, *width=None*, *height=None*, *border=None*, *padding=None*, *align=None*, *font=None*, *colour=None*, *background=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **width** – * **height** – * **border** – * **padding** – * **align** – Horizontal alignment on the page.   **valign** can not be set. * **font** – default font in Header. * **colour** – default foreground colour in Header. * **background** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.Graph


*class* `carmensystems.publisher.api.``Graph`(*discrete=True*, *relwidth=0*)
:   Abstract base class. Graph objects specify how to display data in
    a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart").

    Inheritance

    ![Inheritance diagram of Graph](../../_images/inheritance-953fba8278864fd771fdd6372a28a9f47e51584a.png)

    Methods

    |  |  |
    | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Graph.__init__ "carmensystems.publisher.api.Graph.__init__")([discrete, relwidth]) | Abstract base class; do not initiate. |

    Member details

    `__init__`(*discrete=True*, *relwidth=0*)
    :   Abstract base class; do not initiate.

### carmensystems.publisher.api.Graphic


*class* `carmensystems.publisher.api.``Graphic`
:   Graphic object used for for drawing in a [`Canvas`](carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas"). You cannot construct this, only use instances passed to the [`Canvas.draw()`](carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas.draw "carmensystems.publisher.api.Canvas.draw") method. The coordinate system is initially set to range from (0, 0) to (width-1, height-1), but can be customised using [`coordinates()`](#carmensystems.publisher.api.Graphic.coordinates "carmensystems.publisher.api.Graphic.coordinates").

    Inheritance

    ![Inheritance diagram of Graphic](../../_images/inheritance-6c5ca6cacecc2f6ab78cb55564ba1de3c759a12c.png)

    Methods

    |  |  |
    | --- | --- |
    | [`coordinates`](#carmensystems.publisher.api.Graphic.coordinates "carmensystems.publisher.api.Graphic.coordinates")(self, minx, miny, maxx, maxy) | Set the coordinate system. |
    | [`get_coordinates`](#carmensystems.publisher.api.Graphic.get_coordinates "carmensystems.publisher.api.Graphic.get_coordinates")(self) | Get the boundaries of the coordinate system. |
    | [`image`](#carmensystems.publisher.api.Graphic.image "carmensystems.publisher.api.Graphic.image")(self, x0, y0, path[, width, height, …]) | Insert an image at the given position. |
    | [`image_size`](#carmensystems.publisher.api.Graphic.image_size "carmensystems.publisher.api.Graphic.image_size")(self, path) | Get the amount of space needed by this image. |
    | [`marker`](#carmensystems.publisher.api.Graphic.marker "carmensystems.publisher.api.Graphic.marker")(self, x0, y0, marker[, link, action, …]) | Draw a marker, as specified by the **marker** argument. |
    | [`path`](#carmensystems.publisher.api.Graphic.path "carmensystems.publisher.api.Graphic.path")(self, coords[, width, colour, close, …]) | Draw a line or polygon defined by the points listed in **coords** . |
    | [`rectangle`](#carmensystems.publisher.api.Graphic.rectangle "carmensystems.publisher.api.Graphic.rectangle") | path(self, x0, y0, width, height, linewidth=1, colour=None, fill=None, link=None, action=None, tooltip=None, align=LEFT, valign=TOP) Draw a rectangle starting at (**x0** ,\*\*y0\*\* ). |
    | [`text`](#carmensystems.publisher.api.Graphic.text "carmensystems.publisher.api.Graphic.text")(self, x0, y0, \*texts, \*\*kwds) | Draw text at the given position. |
    | [`text_size`](#carmensystems.publisher.api.Graphic.text_size "carmensystems.publisher.api.Graphic.text_size")(self, \*texts, \*\*kwds) | Get the amount of space needed by this text. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `coordinates`(*self*, *minx*, *miny*, *maxx*, *maxy*)
    :   Set the coordinate system.

    `get_coordinates`(*self*)
    :   Get the boundaries of the coordinate system.

        |  |  |
        | --- | --- |
        | Returns: | a 4-tuple (min-x, min-y, max-x, max-y) |

    `image`(*self*, *x0*, *y0*, *path*, *width=None*, *height=None*, *align=LEFT*, *valign=TOP*, *link=None*, *action=None*, *tooltip=None*)
    :   Insert an image at the given position.

        |  |  |
        | --- | --- |
        | Parameters: | * **x0** – x value of anchoring point * **y0** – y value of anchoring point * **path** (`string`) – path to image file * **align** – where to position **x0** . Default: `LEFT`. * **valign** – where to position **y0** . Default: `TOP`. * **link** – link to another report or webpage. Create with   [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url") or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link"). * **action** – action to trigger when clicking the image.   Create with [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action"). * **tooltip** – tooltip shown when hovering over the image. * **width** (`int`) – the width of the image in the report.   If `None`, it is set relative to **height** .   If **height** is `None` too, width and   height is fetched from the image file. * **height** (`int`) – the height of the image in the report.   If `None`, it is set relative to **width** .   If **width** is `None` too, width and   height is fetched from the image file. |

    `image_size`(*self*, *path*)
    :   Get the amount of space needed by this image.

        |  |  |
        | --- | --- |
        | Parameters: | **path** – path to image file |
        | Returns: | a (width, height) tuple. |

    `marker`(*self*, *x0*, *y0*, *marker*, *link=None*, *action=None*, *tooltip=None*)
    :   Draw a marker, as specified by the **marker** argument.

        |  |  |
        | --- | --- |
        | Parameters: | * **x0** – x value of marker centre. * **y0** – y value of marker centre. * **marker** ([`Marker`](carmensystems.publisher.api.Marker.html#carmensystems.publisher.api.Marker "carmensystems.publisher.api.Marker")) – the marker. * **link** – link to another report or webpage. Use   [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url") or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link"). * **action** – action to trigger when clicking the marker.   Use [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action"). * **tooltip** – tooltip shown when hovering over the marker. |

    `path`(*self*, *coords*, *width=1*, *colour=None*, *close=False*, *fill=None*, *link=None*, *action=None*, *tooltip=None*)
    :   Draw a line or polygon defined by the points listed in **coords** .

        |  |  |
        | --- | --- |
        | Parameters: | * **coords** – A sequence of coordinates, either absolute   ((x,y) tuples) or relative ([`Move`](carmensystems.publisher.api.Move.html#carmensystems.publisher.api.Move "carmensystems.publisher.api.Move")s). First   coordinate (starting point) must be absolute. * **width** (`int`) – line width * **colour** – line colour. A *colour constant* .   Default colour is black, or same color as the fill   colour if that is specified. If however a fill pattern   is specified, the default colour is taken from the colour   of the first line in the pattern. * **close** (`bool`) – close the path, i.e. connect last point to the first   to make a polygon. * **fill** – fill colour or pattern for polygon. Either a   *colour constant* or a [`FillPattern`](carmensystems.publisher.api.FillPattern.html#carmensystems.publisher.api.FillPattern "carmensystems.publisher.api.FillPattern"). * **link** – link to another report or webpage. Create with   [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url") or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link"). * **action** – action to trigger when clicking a polygon.   Create with [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action"). * **tooltip** – tooltip shown when hovering over the polygon. |

    `rectangle`()
    :   path(self, x0, y0, width, height, linewidth=1, colour=None, fill=None, link=None, action=None, tooltip=None, align=LEFT, valign=TOP)
        Draw a rectangle starting at (**x0** ,\*\*y0\*\* ).

        |  |  |
        | --- | --- |
        | Parameters: | * **x0** – x value of anchoring point. * **y0** – y value of anchoring point. * **width** – width of rectangle. * **height** – height of the rectangle. * **linewidth** (`int`) – line (border) width * **colour** – line colour. A *colour constant* .   Default colour is black, or same color as the fill   colour if that is specified. If however a fill pattern   is specified, the default colour is taken from the colour   of the first line in the pattern. * **fill** – fill colour or pattern. Either a I{colour   constant}, a [`Pattern`](carmensystems.publisher.api.Pattern.html#carmensystems.publisher.api.Pattern "carmensystems.publisher.api.Pattern") or an [`ImagePattern`](carmensystems.publisher.api.ImagePattern.html#carmensystems.publisher.api.ImagePattern "carmensystems.publisher.api.ImagePattern"). * **link** – link to another report or webpage. Use   [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url") or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link"). * **action** – action to trigger when clicking the rectangle.   Use [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action"). * **tooltip** – tooltip shown when hovering over the rectangle. * **align** – where to position **x0** . Default: `LEFT`. * **valign** – where to position **y0** . Default: `TOP`. |

    `text`(*self*, *x0*, *y0*, *\*texts*, *\*\*kwds*)
    :   Draw text at the given position.

        |  |  |
        | --- | --- |
        | Parameters: | * **x0** – x value of anchoring point * **y0** – y value of anchoring point * **texts** – Arguments will be concatenated into one string. Items   that are not strings will be converted using `str()`. * **font** ([`Font`](carmensystems.publisher.api.Font.html#carmensystems.publisher.api.Font "carmensystems.publisher.api.Font")) – font to use * **align** – where to position **x0** . Default: `LEFT`. * **valign** – where to position **y0** . Default: `TOP`. * **colour** – text colour. A *colour constant* . * **rotate** (`int`) – text rotation, in degrees. Text can only be rotated   in 90 degree steps. * **link** – link to another report or webpage. Use   [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url") or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link"). * **action** – action to trigger when clicking the text.   Use [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action"). * **tooltip** – tooltip shown when hovering over the text. |

    `text_size`(*self*, *\*texts*, *\*\*kwds*)
    :   Get the amount of space needed by this text.

        |  |  |
        | --- | --- |
        | Parameters: | * **texts** – Arguments will be concatenated into one string. Items   that are not strings will be converted using `str()`. * **font** ([`Font`](carmensystems.publisher.api.Font.html#carmensystems.publisher.api.Font "carmensystems.publisher.api.Font")) – font to use. |
        | Returns: | a (width, height) tuple. |

### carmensystems.publisher.api.Header


*class* `carmensystems.publisher.api.``Header`(*self*, *box*, *\*\*properties*)
:   A running header for the report. Can be added to any [`Column`](carmensystems.publisher.api.Column.html#carmensystems.publisher.api.Column "carmensystems.publisher.api.Column") that is not inside a [`Row`](carmensystems.publisher.api.Row.html#carmensystems.publisher.api.Row "carmensystems.publisher.api.Row").
    The header is active from the next page, or the current page if no output has been generated yet, and until another header is added. The layout of the header is independent of the rest of the page.

    |  |  |
    | --- | --- |
    | Parameters: | * **box** – the box defining the header layout. * **properties** – keyword arguments listed in [`set`](#carmensystems.publisher.api.Header.set "carmensystems.publisher.api.Header.set")can be used. |

    Inheritance

    ![Inheritance diagram of Header](../../_images/inheritance-66abe9dafd2664818a4659965ccd1ae1eb89c782.png)

    Methods

    |  |  |
    | --- | --- |
    | [`add`](#carmensystems.publisher.api.Header.add "carmensystems.publisher.api.Header.add")(self, box) | Add **box** to the end of this Header/Footer, below any previously added boxes. |
    | [`set`](#carmensystems.publisher.api.Header.set "carmensystems.publisher.api.Header.set")(self[, width, height, border, padding, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `add`(*self*, *box*)
    :   Add **box** to the end of this Header/Footer, below any previously added boxes.

    `set`(*self*, *width=None*, *height=None*, *border=None*, *padding=None*, *align=None*, *font=None*, *colour=None*, *background=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **width** – * **height** – * **border** – * **padding** – * **align** – Horizontal alignment on the page.   **valign** can not be set. * **font** – default font in Header. * **colour** – default foreground colour in Header. * **background** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.Image


*class* `carmensystems.publisher.api.``Image`(*self*, *path*, *width=None*, *height=None*, *name=None*, *border=None*, *padding=None*, *align=None*, *valign=None*, *colspan=None*, *rowspan=None*, *background=None*, *bookmark=None*, *link=None*, *action=None*, *tooltip=None*)
:   Box for importing an image file into a report. The only image format currently supported is JPEG.

    See [`set`](#carmensystems.publisher.api.Image.set "carmensystems.publisher.api.Image.set") for a description of the arguments.

    Inheritance

    ![Inheritance diagram of Image](../../_images/inheritance-05fe56bf8aceec007e56b5dd2a17ddd5808ddf2e.png)

    Methods

    |  |  |
    | --- | --- |
    | [`set`](#carmensystems.publisher.api.Image.set "carmensystems.publisher.api.Image.set")(self[, path, width, height, name, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `set`(*self*, *path=None*, *width=None*, *height=None*, *name=None*, *border=None*, *padding=None*, *align=None*, *valign=None*, *colspan=None*, *rowspan=None*, *background=None*, *bookmark=None*, *link=None*, *action=None*, *tooltip=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **path** (`string`) – the path to the image file, relative to either   CARMUSR/images (tried first), CARMADDON\_\*/images or CARMSYS/images. * **width** (`int`) – the width of the image in the report.   If `None`, it is set relative to **height** .   If **height** too is `None`, width and   height is read from the image file. * **height** (`int`) – the height of the image in the report.   If `None`, it is set relative to **width** .   If **width** too is `None`, width and   height is read from the image file. * **name** – * **border** – * **padding** – * **align** – * **valign** – * **colspan** – * **rowspan** – * **background** – colour of the Image’s cell area. The only image   format currently supported is JPEG, so   transparency does not apply. * **bookmark** – * **link** – * **action** – * **tooltip** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.ImagePattern


*class* `carmensystems.publisher.api.``ImagePattern`(*self*, *filename*)
:   Used to fill polygons in a [`Canvas`](carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas"), using an image as pattern.

    |  |  |
    | --- | --- |
    | Parameters: | **filename** (`string`) – the path to the image file, relative to CARMUSR, CARMADDON\_\* or CARMSYS |

    Inheritance

    ![Inheritance diagram of ImagePattern](../../_images/inheritance-e033a6bc64ad6641314737a1b9af41663bd9bf3f.png)

    Methods



    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

### carmensystems.publisher.api.InternalError


*class* `carmensystems.publisher.api.``InternalError`
:   Raised if an internal error is detected. This should be reported as a bug.

    Inheritance

    ![Inheritance diagram of InternalError](../../_images/inheritance-a5b9aa75db1d7d9a78eec1160ddbdb39ccd210cd.png)

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `with_traceback`()
    :   Exception.with\_traceback(tb) –
        set self.\_\_traceback\_\_ to tb and return self.

### carmensystems.publisher.api.Isolate


*class* `carmensystems.publisher.api.``Isolate`(*self*, *box*, *\*\*properties*)
:   Isolates a report component from the rest of the layout

    |  |  |
    | --- | --- |
    | Parameters: | * **box** – the component to isolate; any Box. * **properties** – keyword arguments listed in [`set`](#carmensystems.publisher.api.Isolate.set "carmensystems.publisher.api.Isolate.set")can be used. |

    Inheritance

    ![Inheritance diagram of Isolate](../../_images/inheritance-d2e5e966162b3d174a11076928b3789aa2509613.png)

    Methods

    |  |  |
    | --- | --- |
    | [`set`](#carmensystems.publisher.api.Isolate.set "carmensystems.publisher.api.Isolate.set")(self[, width, height, border, padding, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `set`(*self*, *width=None*, *height=None*, *border=None*, *padding=None*, *align=None*, *valign=None*, *font=None*, *colour=None*, *colspan=None*, *rowspan=None*, *background=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **width** – * **height** – * **border** – * **padding** – * **align** – * **valign** – * **font** – default font for the isolated component. * **colour** – default foreground colour for the isolated   component. * **colspan** – * **rowspan** – * **background** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.Layer


*class* `carmensystems.publisher.api.``Layer`(*yaxis\_name=None*, *yaxis\_limits=(None*, *None)*, *yaxis\_format=None*, *on\_top=True*, *width=1.0*)
:   Abstract base class for a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") data layer.

    Inheritance

    ![Inheritance diagram of Layer](../../_images/inheritance-d4cbd07c7e891eb47d2ef878279e257c3855a350.png)

    Methods

    |  |  |
    | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Layer.__init__ "carmensystems.publisher.api.Layer.__init__")([yaxis\_name, yaxis\_limits, …]) | Abstract base class, do not initiate. |

    Member details

    `__init__`(*yaxis\_name=None*, *yaxis\_limits=(None*, *None)*, *yaxis\_format=None*, *on\_top=True*, *width=1.0*)
    :   Abstract base class, do not initiate.

### carmensystems.publisher.api.Limit


*class* `carmensystems.publisher.api.``Limit`(*linewidth=2*, *colour=None*, *width=1.0*, *offset=None*)
:   Shows [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as limits (horizontal lines).

    Inheritance

    ![Inheritance diagram of Limit](../../_images/inheritance-2fe7ec44754713560c0ee5aadeea681b2fa92fd5.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Limit.__init__ "carmensystems.publisher.api.Limit.__init__")([linewidth, colour, width, offset]) | |  |  | | --- | --- | | param linewidth: | thickness of the line | |

    Member details

    `__init__`(*linewidth=2*, *colour=None*, *width=1.0*, *offset=None*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **linewidth** (`int`) – thickness of the line * **colour** – line colour (*colour constant* ). May also be a   function from the x and y values to a colour, to   have different colours depending on values. * **width** (`float`) – width to use for each data item, in relation to the   available space. 1.0 is all available space. * **offset** (`float`) – positions the left side of the graph in relation   to the available space. You normally   use values in the range 0.0 (inclusive) to 1.0   (exclusive).   0.0 means the graph will be left-justified within   the available space, 1.0 will put it   just outside the available space.  By default, the graph will be centered in the   available space, i.e. the offset will be   0.5 - **width** /2. |

### carmensystems.publisher.api.Line


*class* `carmensystems.publisher.api.``Line`(*width=1*, *colour=None*)
:   Shows [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as a line graph

    Inheritance

    ![Inheritance diagram of Line](../../_images/inheritance-91e057891dee97d76ef68de009b8dfdb8225032a.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Line.__init__ "carmensystems.publisher.api.Line.__init__")([width, colour]) | |  |  | | --- | --- | | param width: | line width | |

    Member details

    `__init__`(*width=1*, *colour=None*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **width** (`int`) – line width * **colour** (*colour constant*) – line colour (*colour constant* ). Unlike [`Marker`](carmensystems.publisher.api.Marker.html#carmensystems.publisher.api.Marker "carmensystems.publisher.api.Marker")   and [`Limit`](carmensystems.publisher.api.Limit.html#carmensystems.publisher.api.Limit "carmensystems.publisher.api.Limit"), the argument cannot be a function,   since the line is common to all data. |

### carmensystems.publisher.api.Marker


*class* `carmensystems.publisher.api.``Marker`(*shape='x'*, *size=6*, *linewidth=1*, *colour=None*)
:   Shows [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as a marker graph.

    Inheritance

    ![Inheritance diagram of Marker](../../_images/inheritance-f667d69794dd3a829317363e89d920cecd6b6ce0.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Marker.__init__ "carmensystems.publisher.api.Marker.__init__")([shape, size, linewidth, colour]) | |  |  | | --- | --- | | param shape: | The shape of the marker. One of: | |

    Member details

    `__init__`(*shape='x'*, *size=6*, *linewidth=1*, *colour=None*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **shape** (`string`) – The shape of the marker. One of:   - `'x'`: cross   - `'+'`: upright cross   - `'d'`: diamond   - `'v'`: angle pointing down   - `'<'`: angle pointing left   - `'>'`: angle pointing right   - `'^'`: angle pointing up * **size** (`int`) – the height and width of the marker.   Note: due to pixel round-off, some sizes may make   the marker look distorted in html. * **linewidth** (`int`) – thickness of lines in marker * **colour** – marker colour (*colour constant* ). When used   in charts, colour may also be a function from   the x and y values to a colour, to have   different colours depending on values. |

### carmensystems.publisher.api.Move


*class* `carmensystems.publisher.api.``Move`(*self*, *x*, *y*)
:   A relative coordinate, to use as a [`path`](carmensystems.publisher.api.Graphic.html#carmensystems.publisher.api.Graphic.path "carmensystems.publisher.api.Graphic.path") component.
    Defines a move from the previous coordinate in the path.
    See the [`Graphic.path()`](carmensystems.publisher.api.Graphic.html#carmensystems.publisher.api.Graphic.path "carmensystems.publisher.api.Graphic.path") method.

    |  |  |
    | --- | --- |
    | Parameters: | * **x** (`int` or `RelTime`) – the value to add to the x value of the previous coordinate. * **y** (`int` or `RelTime`) – the value to add to the y value of the previous coordinate. |

    Inheritance

    ![Inheritance diagram of Move](../../_images/inheritance-91237b9c5ae151e16ffaf62647b234a27e21a151.png)

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

### carmensystems.publisher.api.Pattern


*class* `carmensystems.publisher.api.``Pattern`(*self*, *background=None*)
:   Constructs a pattern used to fill polygons in a [`Canvas`](carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas").

    |  |  |
    | --- | --- |
    | Parameters: | **background** (*colour constant* .) – background colour of the pattern. |

    Inheritance

    ![Inheritance diagram of Pattern](../../_images/inheritance-c1f6496c6c86289c83eeea3fee4cfc651367a96d.png)

    Methods

    |  |  |
    | --- | --- |
    | [`hline`](#carmensystems.publisher.api.Pattern.hline "carmensystems.publisher.api.Pattern.hline")(self, distance[, slant, width, colour]) | Add lines laid out horizontally in the pattern. |
    | [`vline`](#carmensystems.publisher.api.Pattern.vline "carmensystems.publisher.api.Pattern.vline")(self, distance[, slant, width, colour]) | Add lines laid out vertically in the pattern. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `hline`(*self*, *distance*, *slant=0.0*, *width=1*, *colour=None*)
    :   Add lines laid out horizontally in the pattern.

        |  |  |
        | --- | --- |
        | Parameters: | * **distance** – horizontal distance between lines. * **slant** – slant of the lines; how much y is increased for each x unit. **Default value:** 0. * **width** (`int`) – line width * **colour** (*colour constant*) – line colour |

    `vline`(*self*, *distance*, *slant=0.0*, *width=1*, *colour=None*)
    :   Add lines laid out vertically in the pattern.

        |  |  |
        | --- | --- |
        | Parameters: | * **distance** – vertical distance between lines. * **slant** – slant of the lines; how much x is increased for each y unit. **Default value:** 0. * **width** (`int`) – line width * **colour** (*colour constant*) – line colour |

### carmensystems.publisher.api.PublisherError


*class* `carmensystems.publisher.api.``PublisherError`
:   Base class for errors thrown by Publisher. Adds no new functionality.

    Inheritance

    ![Inheritance diagram of PublisherError](../../_images/inheritance-7fcf58ce74106998166b7f4dd8f99fae1c50b32b.png)

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `with_traceback`()
    :   Exception.with\_traceback(tb) –
        set self.\_\_traceback\_\_ to tb and return self.

### carmensystems.publisher.api.Report


*class* `carmensystems.publisher.api.``Report`
:   The entire report. Reports are created by subclassing this class and redefining the `create()` method. Do *not* redefine other methods, including the constructor.

    Inheritance

    ![Inheritance diagram of Report](../../_images/inheritance-1ed9e5651b723c5c9b203e857abf9d4b353d4ef0.png)

    Methods

    |  |  |
    | --- | --- |
    | [`add`](#carmensystems.publisher.api.Report.add "carmensystems.publisher.api.Report.add")(self, box) | Add **box** to the end of this Column, below any previously added boxes. |
    | [`add_footer`](#carmensystems.publisher.api.Report.add_footer "carmensystems.publisher.api.Report.add_footer")(self, box[, column]) | |  |  | | --- | --- | | param box: | the component to use as footer; any Box. | |
    | [`add_header`](#carmensystems.publisher.api.Report.add_header "carmensystems.publisher.api.Report.add_header")(self, box[, column]) | |  |  | | --- | --- | | param box: | the component to use as header; any Box. | |
    | [`arg`](#carmensystems.publisher.api.Report.arg "carmensystems.publisher.api.Report.arg")(self, paramname) | Get the value of a parameter passed to the report via the **params** argument to [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link") or [`chartlink()`](carmensystems.publisher.api.chartlink.html#carmensystems.publisher.api.chartlink "carmensystems.publisher.api.chartlink"), or the **reportparams** argument to [`generateReport()`](carmensystems.publisher.api.generateReport.html#carmensystems.publisher.api.generateReport "carmensystems.publisher.api.generateReport"). |
    | [`bufferarg`](#carmensystems.publisher.api.Report.bufferarg "carmensystems.publisher.api.Report.bufferarg")(self) | Get a handle (proxy) to the application buffer or context locator passed to the report via the **context** argument to [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link"), [`chartlink()`](carmensystems.publisher.api.chartlink.html#carmensystems.publisher.api.chartlink "carmensystems.publisher.api.chartlink") or [`generateReport()`](carmensystems.publisher.api.generateReport.html#carmensystems.publisher.api.generateReport "carmensystems.publisher.api.generateReport"). |
    | [`create`](#carmensystems.publisher.api.Report.create "carmensystems.publisher.api.Report.create")(self) | Creates the entire Report. |
    | [`newpage`](#carmensystems.publisher.api.Report.newpage "carmensystems.publisher.api.Report.newpage")(self) | Hard page break: Always add a page break at this place in the column. |
    | [`page`](#carmensystems.publisher.api.Report.page "carmensystems.publisher.api.Report.page")(self) | Soft page break, high priority: Add a page break at this place in the column if all content up to the next [`newpage()`](carmensystems.publisher.api.Column.html#carmensystems.publisher.api.Column.newpage "carmensystems.publisher.api.Column.newpage") or page() will not fit into the current page. |
    | [`page0`](#carmensystems.publisher.api.Report.page0 "carmensystems.publisher.api.Report.page0")(self) | Soft page break, low priority: Add a page break at this place in the column if all content up to the next page break – of any priority – will not fit into the current page. |
    | [`page_width`](#carmensystems.publisher.api.Report.page_width "carmensystems.publisher.api.Report.page_width")(self) | Returns the width of the page minus margins. |
    | [`set`](#carmensystems.publisher.api.Report.set "carmensystems.publisher.api.Report.set")(self[, border, font, colour, …]) | Set component properties. |
    | [`setpaper`](#carmensystems.publisher.api.Report.setpaper "carmensystems.publisher.api.Report.setpaper")(self, orientation[, size]) | |  |  | | --- | --- | | param orientation: | valid values are module constants `PORTRAIT` | |

    Attributes

    |  |  |
    | --- | --- |
    | `p_id` |  |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `add`(*self*, *box*)
    :   Add **box** to the end of this Column, below any previously added boxes.

    `add_footer`(*self*, *box*, *column=self*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **box** – the component to use as footer; any Box. * **column** – The column to which this footer belongs, default is self. |

    `add_header`(*self*, *box*, *column=self*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **box** – the component to use as header; any Box. * **column** – The column to which this header belongs, default is self. |

    `arg`(*self*, *paramname*)
    :   Get the value of a parameter passed to the report via the
        **params** argument to [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link") or [`chartlink()`](carmensystems.publisher.api.chartlink.html#carmensystems.publisher.api.chartlink "carmensystems.publisher.api.chartlink"), or the **reportparams**
        argument to [`generateReport()`](carmensystems.publisher.api.generateReport.html#carmensystems.publisher.api.generateReport "carmensystems.publisher.api.generateReport").

        |  |  |
        | --- | --- |
        | Parameters: | **paramname** (`string`) – Name of the parameter |
        | Returns: | the parameter value, or `None` if no such parameter has been passed to the report. |
        | Return type: | `string` |

    `bufferarg`(*self*)
    :   Get a handle (proxy) to the application buffer or context locator passed to the report via the **context** argument to [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link"), [`chartlink()`](carmensystems.publisher.api.chartlink.html#carmensystems.publisher.api.chartlink "carmensystems.publisher.api.chartlink") or [`generateReport()`](carmensystems.publisher.api.generateReport.html#carmensystems.publisher.api.generateReport "carmensystems.publisher.api.generateReport"). The value can be used as an argument to `carmensystems.rave.api.buffer2context()`

        |  |  |
        | --- | --- |
        | Returns: | A proxy for the application buffer or context locator, or `None` if no object was provided. |

    `create`(*self*)
    :   Creates the entire Report. This method gets called during
        report generation, and should build the entire report structure.

        |  |  |
        | --- | --- |
        | Raises: | **NotImplementedError** – always. Must be redefined in subclasses. |

    `newpage`(*self*)
    :   Hard page break: Always add a page break at this place in the column.

    `page`(*self*)
    :   Soft page break, high priority: Add a page break at this place in the column if all content up to the next [`newpage()`](carmensystems.publisher.api.Column.html#carmensystems.publisher.api.Column.newpage "carmensystems.publisher.api.Column.newpage") or page() will not fit into the current page.

    `page0`(*self*)
    :   Soft page break, low priority: Add a page break at this place in the column if all content up to the next page break – of any priority – will not fit into the current page.

    `page_width`(*self*)
    :   Returns the width of the page minus margins. If paper margins is specified, it must be done before calling this function.

    `set`(*self*, *border=None*, *font=None*, *colour=None*, *background=None*, *margins=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **border** – * **font** – default font for the entire report. * **colour** – default foreground colour for the entire report. * **background** – default background colour for the entire report. * **margins** – set page margins for the report. Use function   [`padding()`](carmensystems.publisher.api.padding.html#carmensystems.publisher.api.padding "carmensystems.publisher.api.padding") to specify margins.  The default margins for PDF are (left to bottom, clockwise): 42, 36, 36, 36. HTML margins are set in the browser. |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various properties.

    `setpaper`(*self*, *orientation*, *size=A4*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **orientation** – valid values are module constants `PORTRAIT`or `LANDSCAPE`. * **size** – paper size. Valid values are the following module constants:    + `LETTER`   + `LEGAL`   + `A4`   + `A3`   + `B5`   + `C5`   + `DL`   + `EXECUTIVE` `A4` is default. |

### carmensystems.publisher.api.ReportMetadata


*class* `carmensystems.publisher.api.``ReportMetadata`(*report\_name*, *report\_description=None*, *formats=('HTML'*, *'PDF')*, *parameters=[]*)
:   Report metadata, to be provided by a `get_report_metadata()` function in the report module,
    and used by potential callers.

    **Note:** This is an Atrium-only feature (not supported in Studio).

    Inheritance

    ![Inheritance diagram of ReportMetadata](../../_images/inheritance-5da77943958ddf6346262218512a1f50718762c8.png)



    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.ReportMetadata.__init__ "carmensystems.publisher.api.ReportMetadata.__init__")(report\_name[, report\_description, …]) | |  |  | | --- | --- | | param report\_name: | Readable name, will be used in presentation strings menus etc. | |

    Member details

    `__init__`(*report\_name*, *report\_description=None*, *formats=('HTML'*, *'PDF')*, *parameters=[]*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **report\_name** – Readable name, will be used in presentation strings menus etc. * **report\_description** – Description of what the report does * **formats** – Output formats supported by the report * **parameters** – [`ReportParameter`](carmensystems.publisher.api.ReportParameter.html#carmensystems.publisher.api.ReportParameter "carmensystems.publisher.api.ReportParameter")s for the report |

### carmensystems.publisher.api.ReportParameter


*class* `carmensystems.publisher.api.``ReportParameter`(*parameter\_id*, *parameter\_type*, *display\_name=None*, *description=None*, *constraint=None*, *default\_value=None*, *required=True*)
:   A parameter that the report is expecting to receive when called.

    For example, selection parameters such as date, select, multiselect, etc.

    **Note:** This is an Atrium-only feature (not supported in Studio).

    Inheritance

    ![Inheritance diagram of ReportParameter](../../_images/inheritance-9122beb39d2d37e600a1531d40c48507728d3fa0.png)



    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.ReportParameter.__init__ "carmensystems.publisher.api.ReportParameter.__init__")(parameter\_id, parameter\_type[, …]) | |  |  | | --- | --- | | param parameter\_id: | Technical name of the parameter | |

    Member details

    `__init__`(*parameter\_id*, *parameter\_type*, *display\_name=None*, *description=None*, *constraint=None*, *default\_value=None*, *required=True*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **parameter\_id** – Technical name of the parameter * **parameter\_type** – Technical mapping to widgets used when editing this parameter * **display\_name** – Readable name of the parameter * **description** – Description of the impact of the parameter * **constraint** – Parameter value constraint * **default\_value** – Default value for the parameter * **required** – If the parameter needs to be specified or if it is optional |

### carmensystems.publisher.api.Row


*class* `carmensystems.publisher.api.``Row`(*self*, *\*components*, *\*\*properties*)
:   Components laid out horizontally.

    |  |  |
    | --- | --- |
    | Parameters: | * **components** – components of the row. More components can   be added with the [`add()`](#carmensystems.publisher.api.Row.add "carmensystems.publisher.api.Row.add") method. * **properties** – keyword arguments listed in [`set`](#carmensystems.publisher.api.Row.set "carmensystems.publisher.api.Row.set")can be used. |

    Inheritance

    ![Inheritance diagram of Row](../../_images/inheritance-640e856612cae540c4a5b6d5a1e388250eb6b328.png)

    Methods

    |  |  |
    | --- | --- |
    | [`add`](#carmensystems.publisher.api.Row.add "carmensystems.publisher.api.Row.add")(self, box) | Add **box** to the end of this Row, to the right of any previously added boxes. |
    | [`set`](#carmensystems.publisher.api.Row.set "carmensystems.publisher.api.Row.set")(self[, height, border, font, colour, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `add`(*self*, *box*)
    :   Add **box** to the end of this Row, to the right of any previously added boxes.

    `set`(*self*, *height=None*, *border=None*, *font=None*, *colour=None*, *rowspan=None*, *background=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **height** – minimum height of the Row, even if the Row   is empty. **width** can not be set. * **border** – * **font** – default font for components in the Row. * **colour** – default foreground colour for components in   the Row. * **rowspan** – minimum colspan of Row, even if it is empty.   **colspan** can not be set. * **background** – default background colour for components in   the Row. |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.Series


*class* `carmensystems.publisher.api.``Series`(*data*, *yaxis\_name=None*, *yaxis\_limits=(None*, *None)*, *yaxis\_format=None*, *graph=None*, *label=None*, *legends=[]*, *link=None*, *action=None*, *tooltip=None*)
:   A set of (x, y) values to display in a [`Chart`](carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart").

    Inheritance

    ![Inheritance diagram of Series](../../_images/inheritance-3b545903d84850bb7f3bbfcc21d3c2d4c7f85118.png)

    Methods

    |  |  |  |  |
    | --- | --- | --- | --- |
    | [`__init__`](#carmensystems.publisher.api.Series.__init__ "carmensystems.publisher.api.Series.__init__")(data[, yaxis\_name, yaxis\_limits, …]) | |  |  | | --- | --- | | param data: | a `list` of (x,y) values. | |
    | [`aggregate`](#carmensystems.publisher.api.Series.aggregate "carmensystems.publisher.api.Series.aggregate")(x, ys) | Redefine to change behaviour for multiple values for the same x value |

    Member details

    `__init__`(*data*, *yaxis\_name=None*, *yaxis\_limits=(None*, *None)*, *yaxis\_format=None*, *graph=None*, *label=None*, *legends=[]*, *link=None*, *action=None*, *tooltip=None*)
    :   |  |  |
        | --- | --- |
        | Parameters: | * **data** – a `list` of (x,y) values.   x values may have type `int`, `float`, `AbsTime` or `str`.   y values may be `int` or `float`. Ints and floats   can be mixed on the same axis, other types cannot be mixed. * **yaxis\_name** (`string`) – y-axis label. * **yaxis\_limits** (`tuple`) – a (min,max) tuple specifying min and max   values for the y-axis. To set only min or   only max, set the other value to `None`.   The limits may be pushed to include all values,   and to fit the placing of the tick marks. * **yaxis\_format** (`function`) – formatting function to use when writing   values on the tick marks. Should take a   y value and return a `string` * **graph** – a subclass of [`Graph`](carmensystems.publisher.api.Graph.html#carmensystems.publisher.api.Graph "carmensystems.publisher.api.Graph"), specifying how   data is displayed. * **label** (`string`) – label the data. Will produce a   legend using the graph colour. * **legends** – a list of (label, colour) 2-tuples defining   legends for the chart. Labels are strings,   colours are *colour constant* s.   If this is set, **label** will be ignored.   Useful if a data set uses different colours   depending on the value. * **link** – link from data items to another report or   webpage. Use [`charturl()`](carmensystems.publisher.api.charturl.html#carmensystems.publisher.api.charturl "carmensystems.publisher.api.charturl") or [`chartlink()`](carmensystems.publisher.api.chartlink.html#carmensystems.publisher.api.chartlink "carmensystems.publisher.api.chartlink")   to make the link depend on the data;   use [`url()`](carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url") or [`link()`](carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link") to have the same   link on all data items. * **action** – action to trigger when clicking a data item.   Use [`chartaction()`](carmensystems.publisher.api.chartaction.html#carmensystems.publisher.api.chartaction "carmensystems.publisher.api.chartaction") to make the action   depend on the data; use [`action()`](carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action") to have   the same action on all data items. * **tooltip** – tooltip to show when hovering over a data item.   Use [`charttooltip`](carmensystems.publisher.api.charttooltip.html#carmensystems.publisher.api.charttooltip "carmensystems.publisher.api.charttooltip") to make the tooltip. |

    `aggregate`(*x*, *ys*)
    :   Redefine to change behaviour for multiple values for the same x value

### carmensystems.publisher.api.Text


*class* `carmensystems.publisher.api.``Text`(*self*, *\*texts*, *\*\*properties*)
:   A Text box

    |  |  |
    | --- | --- |
    | Parameters: | * **texts** – Any number of `string`s, [`Crossref`](carmensystems.publisher.api.Crossref.html#carmensystems.publisher.api.Crossref "carmensystems.publisher.api.Crossref")s or other objects.   Arguments that are neither strings nor Crossrefs are   converted to a string using `str()`. The resulting   strings are concatenated.  Tabs, newlines and other formatting characters are   ignored. The text can be made to wrap by setting the   **width** property. * **properties** – keyword arguments listed in [`set`](#carmensystems.publisher.api.Text.set "carmensystems.publisher.api.Text.set")can be used. |

    Inheritance

    ![Inheritance diagram of Text](../../_images/inheritance-c4bd1af89cb712109bd09ea6103c5e545f815e54.png)

    Methods

    |  |  |
    | --- | --- |
    | [`set`](#carmensystems.publisher.api.Text.set "carmensystems.publisher.api.Text.set")(self[, width, height, name, border, …]) | Set component properties. |

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `set`(*self*, *width=None*, *height=None*, *name=None*, *border=None*, *padding=None*, *align=None*, *valign=None*, *font=None*, *colour=None*, *colspan=None*, *rowspan=None*, *background=None*, *bookmark=None*, *link=None*, *action=None*, *tooltip=None*)
    :   Set component properties.

        |  |  |
        | --- | --- |
        | Parameters: | * **width** – * **height** – * **name** – * **border** – * **padding** – default is `padding(2,2,2,2)` * **align** – * **valign** – * **font** – * **colour** – * **colspan** – * **rowspan** – * **background** – * **bookmark** – * **link** – * **action** – * **tooltip** – |

        See: [`Box.set()`](carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box.set "carmensystems.publisher.api.Box.set") for more details on the various
        :   properties.

### carmensystems.publisher.api.UsageError


*class* `carmensystems.publisher.api.``UsageError`
:   Raised on errors caused by the user.

    Inheritance

    ![Inheritance diagram of UsageError](../../_images/inheritance-ecc950e766d39ba352cab054b2b0b5abadce3793.png)

    Member details

    `__init__`
    :   Initialize self. See help(type(self)) for accurate signature.

    `with_traceback`()
    :   Exception.with\_traceback(tb) –
        set self.\_\_traceback\_\_ to tb and return self.