# carmensystems.publisher.api — Python Report Toolkit API


This module provides an API for reports.

### Class summary

|  |  |
| --- | --- |
| [`Area`](stubs/carmensystems.publisher.api.Area.html#carmensystems.publisher.api.Area "carmensystems.publisher.api.Area")([fill]) | Shows [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as an area graph: like a [`Line`](stubs/carmensystems.publisher.api.Line.html#carmensystems.publisher.api.Line "carmensystems.publisher.api.Line") graph, except the area under the line is filled. |
| [`Bar`](stubs/carmensystems.publisher.api.Bar.html#carmensystems.publisher.api.Bar "carmensystems.publisher.api.Bar")([fill, width, offset]) | Shows [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as bar graphs. |
| [`Box`](stubs/carmensystems.publisher.api.Box.html#carmensystems.publisher.api.Box "carmensystems.publisher.api.Box") | Abstract base class for all report components. |
| [`CSVReport`](stubs/carmensystems.publisher.api.CSVReport.html#carmensystems.publisher.api.CSVReport "carmensystems.publisher.api.CSVReport")([outputfile, reportparams, context]) | Base class to use for creating CSV reports. |
| [`Canvas`](stubs/carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas")(self, width, height, \*\*properties) | A user-defined drawing. |
| [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart")(width, height, \*layers, \*\*properties) | A graphic chart: show values in a coordinate system using bar graphs, line graphs etc. |
| [`ColourPalette`](stubs/carmensystems.publisher.api.ColourPalette.html#carmensystems.publisher.api.ColourPalette "carmensystems.publisher.api.ColourPalette")(\*\*colourmap) | Define a colour palette for use in a Report. |
| [`Column`](stubs/carmensystems.publisher.api.Column.html#carmensystems.publisher.api.Column "carmensystems.publisher.api.Column")(self, \*components, \*\*properties) | Components laid out vertically. |
| [`Combine`](stubs/carmensystems.publisher.api.Combine.html#carmensystems.publisher.api.Combine "carmensystems.publisher.api.Combine")(\*layers, \*\*properties) | Combine several layers of [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") data in the same coordinate system. |
| [`Container`](stubs/carmensystems.publisher.api.Container.html#carmensystems.publisher.api.Container "carmensystems.publisher.api.Container") | Abstract base class for boxes that align several other boxes |
| [`Crossref`](stubs/carmensystems.publisher.api.Crossref.html#carmensystems.publisher.api.Crossref "carmensystems.publisher.api.Crossref")(self, name[, size, format]) | Creates a cross reference or an internal link to a page number or to a named component elsewhere in the report. |
| [`Expandable`](stubs/carmensystems.publisher.api.Expandable.html#carmensystems.publisher.api.Expandable "carmensystems.publisher.api.Expandable")(self, header, body, \*\*properties) | In interactive output, creates a control (header) which lets the user control the visibility of an expandable section (body). |
| [`FillPattern`](stubs/carmensystems.publisher.api.FillPattern.html#carmensystems.publisher.api.FillPattern "carmensystems.publisher.api.FillPattern") | Base class for patterns used to fill polygons in a [`Canvas`](stubs/carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas"). |
| [`Footer`](stubs/carmensystems.publisher.api.Footer.html#carmensystems.publisher.api.Footer "carmensystems.publisher.api.Footer")(self, box, \*\*properties) | A running footer for the report. |
| [`Graph`](stubs/carmensystems.publisher.api.Graph.html#carmensystems.publisher.api.Graph "carmensystems.publisher.api.Graph")([discrete, relwidth]) | Abstract base class. |
| [`Graphic`](stubs/carmensystems.publisher.api.Graphic.html#carmensystems.publisher.api.Graphic "carmensystems.publisher.api.Graphic") | Graphic object used for for drawing in a [`Canvas`](stubs/carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas"). |
| [`Header`](stubs/carmensystems.publisher.api.Header.html#carmensystems.publisher.api.Header "carmensystems.publisher.api.Header")(self, box, \*\*properties) | A running header for the report. |
| [`Image`](stubs/carmensystems.publisher.api.Image.html#carmensystems.publisher.api.Image "carmensystems.publisher.api.Image")(self, path[, width, height, name, …]) | Box for importing an image file into a report. |
| [`ImagePattern`](stubs/carmensystems.publisher.api.ImagePattern.html#carmensystems.publisher.api.ImagePattern "carmensystems.publisher.api.ImagePattern")(self, filename) | Used to fill polygons in a [`Canvas`](stubs/carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas"), using an image as pattern. |
| [`InternalError`](stubs/carmensystems.publisher.api.InternalError.html#carmensystems.publisher.api.InternalError "carmensystems.publisher.api.InternalError") | Raised if an internal error is detected. |
| [`Isolate`](stubs/carmensystems.publisher.api.Isolate.html#carmensystems.publisher.api.Isolate "carmensystems.publisher.api.Isolate")(self, box, \*\*properties) | Isolates a report component from the rest of the layout |
| [`Layer`](stubs/carmensystems.publisher.api.Layer.html#carmensystems.publisher.api.Layer "carmensystems.publisher.api.Layer")([yaxis\_name, yaxis\_limits, …]) | Abstract base class for a [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") data layer. |
| [`Limit`](stubs/carmensystems.publisher.api.Limit.html#carmensystems.publisher.api.Limit "carmensystems.publisher.api.Limit")([linewidth, colour, width, offset]) | Shows [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as limits (horizontal lines). |
| [`Line`](stubs/carmensystems.publisher.api.Line.html#carmensystems.publisher.api.Line "carmensystems.publisher.api.Line")([width, colour]) | Shows [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as a line graph |
| [`Marker`](stubs/carmensystems.publisher.api.Marker.html#carmensystems.publisher.api.Marker "carmensystems.publisher.api.Marker")([shape, size, linewidth, colour]) | Shows [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") values as a marker graph. |
| [`Move`](stubs/carmensystems.publisher.api.Move.html#carmensystems.publisher.api.Move "carmensystems.publisher.api.Move")(self, x, y) | A relative coordinate, to use as a [`path`](stubs/carmensystems.publisher.api.Graphic.html#carmensystems.publisher.api.Graphic.path "carmensystems.publisher.api.Graphic.path") component. |
| [`Pattern`](stubs/carmensystems.publisher.api.Pattern.html#carmensystems.publisher.api.Pattern "carmensystems.publisher.api.Pattern")(self[, background]) | Constructs a pattern used to fill polygons in a [`Canvas`](stubs/carmensystems.publisher.api.Canvas.html#carmensystems.publisher.api.Canvas "carmensystems.publisher.api.Canvas"). |
| [`PublisherError`](stubs/carmensystems.publisher.api.PublisherError.html#carmensystems.publisher.api.PublisherError "carmensystems.publisher.api.PublisherError") | Base class for errors thrown by Publisher. |
| [`Report`](stubs/carmensystems.publisher.api.Report.html#carmensystems.publisher.api.Report "carmensystems.publisher.api.Report") | The entire report. |
| [`ReportMetadata`](stubs/carmensystems.publisher.api.ReportMetadata.html#carmensystems.publisher.api.ReportMetadata "carmensystems.publisher.api.ReportMetadata")(report\_name[, …]) | Report metadata, to be provided by a `get_report_metadata()` function in the report module, and used by potential callers. |
| [`ReportParameter`](stubs/carmensystems.publisher.api.ReportParameter.html#carmensystems.publisher.api.ReportParameter "carmensystems.publisher.api.ReportParameter")(parameter\_id, parameter\_type) | A parameter that the report is expecting to receive when called. |
| [`Row`](stubs/carmensystems.publisher.api.Row.html#carmensystems.publisher.api.Row "carmensystems.publisher.api.Row")(self, \*components, \*\*properties) | Components laid out horizontally. |
| [`Series`](stubs/carmensystems.publisher.api.Series.html#carmensystems.publisher.api.Series "carmensystems.publisher.api.Series")(data[, yaxis\_name, yaxis\_limits, …]) | A set of (x, y) values to display in a [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart"). |
| [`Text`](stubs/carmensystems.publisher.api.Text.html#carmensystems.publisher.api.Text "carmensystems.publisher.api.Text")(self, \*texts, \*\*properties) | A Text box |
| [`UsageError`](stubs/carmensystems.publisher.api.UsageError.html#carmensystems.publisher.api.UsageError "carmensystems.publisher.api.UsageError") | Raised on errors caused by the user. |

### Functions

|  |  |
| --- | --- |
| [`Font`](stubs/carmensystems.publisher.api.Font.html#carmensystems.publisher.api.Font "carmensystems.publisher.api.Font")([face, size, weight, style]) | Synonym for [`font()`](stubs/carmensystems.publisher.api.font.html#carmensystems.publisher.api.font "carmensystems.publisher.api.font"). |
| [`action`](stubs/carmensystems.publisher.api.action.html#carmensystems.publisher.api.action "carmensystems.publisher.api.action")(function[, args]) | Creates an action for a component. |
| [`bookmark`](stubs/carmensystems.publisher.api.bookmark.html#carmensystems.publisher.api.bookmark "carmensystems.publisher.api.bookmark")(text[, level, open]) | PDF only: create a bookmark for a component. |
| [`border`](stubs/carmensystems.publisher.api.border.html#carmensystems.publisher.api.border "carmensystems.publisher.api.border")([left, top, right, bottom, …]) | Create a border around a component’s cell area, and optionally between nested components. |
| [`border_all`](stubs/carmensystems.publisher.api.border_all.html#carmensystems.publisher.api.border_all "carmensystems.publisher.api.border_all")([w, colour]) | Shorthand for :obj:`` `border ``<border>```(left=w, top=w, right=w, bottom=w, inner\_floor=w, inner\_wall=w, colour=colour)``. |
| [`border_frame`](stubs/carmensystems.publisher.api.border_frame.html#carmensystems.publisher.api.border_frame "carmensystems.publisher.api.border_frame")([w, colour]) | Shorthand for :obj:`` `border ``<border>```(left=w, top=w, right=w, bottom=w, colour=colour)`` |
| [`chartaction`](stubs/carmensystems.publisher.api.chartaction.html#carmensystems.publisher.api.chartaction "carmensystems.publisher.api.chartaction")(fun) | Creates an action for a graphic object in a [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart"), e.g. |
| [`chartlink`](stubs/carmensystems.publisher.api.chartlink.html#carmensystems.publisher.api.chartlink "carmensystems.publisher.api.chartlink")(module[, params, context]) | Create a link from a graphic object in a [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") to another Publisher report. |
| [`charttooltip`](stubs/carmensystems.publisher.api.charttooltip.html#carmensystems.publisher.api.charttooltip "carmensystems.publisher.api.charttooltip")(fun) | Creates a tooltip for a graphic object in a [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart"), e.g. |
| [`charturl`](stubs/carmensystems.publisher.api.charturl.html#carmensystems.publisher.api.charturl "carmensystems.publisher.api.charturl")(url[, params]) | Create a link from a graphic object in a [`Chart`](stubs/carmensystems.publisher.api.Chart.html#carmensystems.publisher.api.Chart "carmensystems.publisher.api.Chart") to a webpage. |
| [`errmsg`](stubs/carmensystems.publisher.api.errmsg.html#carmensystems.publisher.api.errmsg "carmensystems.publisher.api.errmsg")(source, err) | Format error message with a message consisting of report name, exception text and stack trace. |
| [`font`](stubs/carmensystems.publisher.api.font.html#carmensystems.publisher.api.font "carmensystems.publisher.api.font")([face, size, weight, style]) | Create a font object. |
| [`generateReport`](stubs/carmensystems.publisher.api.generateReport.html#carmensystems.publisher.api.generateReport "carmensystems.publisher.api.generateReport")(source, outputfile[, format, …]) | Render a report in the specified format and save it in **outputfile** . |
| [`get_supported_report_class`](stubs/carmensystems.publisher.api.get_supported_report_class.html#carmensystems.publisher.api.get_supported_report_class "carmensystems.publisher.api.get_supported_report_class")(module\_name) | Return the class of the report. |
| [`javascriptAction`](stubs/carmensystems.publisher.api.javascriptAction.html#carmensystems.publisher.api.javascriptAction "carmensystems.publisher.api.javascriptAction")(function) | Creates a javascript action for a component. |
| [`link`](stubs/carmensystems.publisher.api.link.html#carmensystems.publisher.api.link "carmensystems.publisher.api.link")(module[, params, context]) | Create a link from a component to another Publisher report. |
| [`padding`](stubs/carmensystems.publisher.api.padding.html#carmensystems.publisher.api.padding "carmensystems.publisher.api.padding")([left, top, right, bottom]) | Create padding (space between border and content) for a component. |
| [`render`](stubs/carmensystems.publisher.api.render.html#carmensystems.publisher.api.render "carmensystems.publisher.api.render")(report, format) |  |
| [`url`](stubs/carmensystems.publisher.api.url.html#carmensystems.publisher.api.url "carmensystems.publisher.api.url")(path[, params]) | Create a link from a component to an internet page. |

### Variables

#### Document format

`carmensystems.publisher.api.``CSV`

`carmensystems.publisher.api.``HTML`

`carmensystems.publisher.api.``PDF`

`carmensystems.publisher.api.``TXT`

#### Paper size

`carmensystems.publisher.api.``A3`

`carmensystems.publisher.api.``A4`

`carmensystems.publisher.api.``B5`

`carmensystems.publisher.api.``C5`

`carmensystems.publisher.api.``DL`

`carmensystems.publisher.api.``EXECUTIVE`

`carmensystems.publisher.api.``LEGAL`

`carmensystems.publisher.api.``LETTER`

#### Page orientation

`carmensystems.publisher.api.``LANDSCAPE`

`carmensystems.publisher.api.``PORTRAIT`

#### Alignment

`carmensystems.publisher.api.``BOTTOM`

`carmensystems.publisher.api.``CENTER`

`carmensystems.publisher.api.``LEFT`

`carmensystems.publisher.api.``RIGHT`

`carmensystems.publisher.api.``TOP`

#### Font face

`carmensystems.publisher.api.``MONOSPACE`

`carmensystems.publisher.api.``SANSSERIF`

`carmensystems.publisher.api.``SERIF`

#### Font style

`carmensystems.publisher.api.``BOLD`

`carmensystems.publisher.api.``ITALIC`
