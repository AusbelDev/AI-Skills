# Geometrical model


This chapter contains a description of the geometrical model of the PRT API.

* [Overview](#overview)
* [Objects](#objects)
  + [Text](#text)
  + [Isolate](#isolate)
  + [Image, Canvas, Chart](#image-canvas-chart)
  + [Row, Column](#row-column)
  + [Header](#header)
  + [Footer](#footer)
  + [Crossref](#crossref)
  + [Report](#report)
  + [Expandable](#expandable)
* [Properties](#properties)
  + [width, height](#width-height)
  + [align, valign](#align-valign)
  + [colspan, rowspan](#colspan-rowspan)
  + [Empty cells](#empty-cells)
  + [padding](#padding)
  + [font, colour](#font-colour)
  + [background](#background)
  + [border](#border)
  + [action, link, url](#action-link-url)
* [Page definition](#page-definition)
  + [Margins](#margins)
  + [Page width](#page-width)
  + [Paper size](#paper-size)
  + [PDF page breaks](#pdf-page-breaks)
  + [HTML page breaks](#html-page-breaks)

### [2.1. Overview](#id7)

The PRT API consists of a number of objects, placed on a grid, that are used to create the
report. The geometrical model describes how properties (attributes) affect the layout of
these objects. There are two main types of objects in PRT:

* atom objects (do not contain other objects)
* container objects (may contain other objects)

All objects have an object area and a cell area. The cell area is always expanded to fill
the available space in the grid, while the object area can only be expanded by the objects
inside it.

The cell width is set by the widest component in the cell’s column of the grid, and the
height is set by the highest component in the row.

Each object also has a set of properties. All properties are not applicable to all
objects. This is further described in [2.3](#prt-properties).

### [2.2. Objects](#id8)

#### [2.2.1. Text](#id9)

Text is an atom object, and the actual text flows inside the object area.

The width for a Text object is set on the object area and is the same as the maximum
width, while the height is only a minimum height. If the length of the text exceeds the
specified width, a line break is added to the text. Because of that, the height of the
object area in the Text object cannot be set to a max value.

If no width is specified, the width of the object area is adjusted to the width of the
written text.

The minimum value for the width of the Text is set to be the length of the longest word in
the text. Words are not broken.

However, the cell width can exceed the specified width. If the cell width is greater than
the width of the object area, the object area does not fill the entire cell.

#### [2.2.2. Isolate](#id10)

Isolate is a container object that is used for isolating the contained object from the
surrounding layout (an Isolate object has its own separate grid).

An object area contained in an Isolate object is not aligned with the surrounding layout,
while the cell area is still aligned with the surrounding layout.

The size of the object area is decided by the minimum value of the specified values for
Isolate or the size of the included objects inside the object area.

Properties are inherited by the objects contained in Isolate.

#### [2.2.3. Image, Canvas, Chart](#id11)

Image, Canvas and Chart are all atoms, which means that they contain only one single
object in the object area. Compare with Isolate.

The size of the object area is specified explicitly and cannot be altered by the included
object. The specified width and height are maximum values.

#### [2.2.4. Row, Column](#id12)

Row and Column are both container objects, but unlike Isolate they do not have an object
area. They are used for grouping and aligning other objects.

Since Row and Column only have a cell area, width and height are set on the cell area
instead of the object area. The values are minimum values and can be expanded by the
included objects or the surrounding layout.

Even if Row and Column do not have an object area, you can still set some object
attributes. These attributes are inherited by the objects contained in the Row/Column.
Columns can have independent headers and footers that behave similarly to headers and
footers on Report.

#### [2.2.5. Header](#id13)

Header defines a running header on a Report.

#### [2.2.6. Footer](#id14)

Footer defines a running footer on a Report.

#### [2.2.7. Crossref](#id15)

A Crossref is a not a regular component; it can be used as a part of a Text component
referring to another named component or page number.

#### [2.2.8. Report](#id16)

This is the top-level object that holds the entire report.

#### [2.2.9. Expandable](#id17)

A class that creates a component that lets the user control the visibility of certain information in interactive (HTML) output. In non-interactive output formats, this information is always visible.

### [2.3. Properties](#id18)

Properties can be either cell properties or object properties. Cell properties have the cell as scope while the scope for the object attributes is the object inside the cell.

Properties are set using the Box.set() method or with keyword arguments to the constructors.

#### [2.3.1. width, height](#id19)

width and height define the size of the object and are measured in points (1/72 inch). The meaning of width and height varies for different types of objects. In general they are object attributes and define the size of the object area inside a cell.

##### 2.3.1.1. Text

For Text, the width is a maximum value, while height is minimum value of the object area. If a text inside the object area becomes wider than the specified width, a line break is added to the text. If no width is specified the text is displayed in one row, that is no line breaks.

* object-area-width = specified-width
* object-area-height = max (specified-height, lines-height)
* cell-area-size = max (grid-size, object-area-size + padding)

##### 2.3.1.2. Isolate

For Isolate, width and height are minimum values of the object area. The size of the object area can be expanded if the objects contained in object area are wider/higher than the specified width/height.
\* object-area-size = max (width\_and\_height-size, included-objects-size)
\* cell\_area\_size = max (grid-size, object-area-size + padding)

##### 2.3.1.3. Image, Canvas, Chart

Width and height are values for the object area. The size of the object area must be specified explicitly for Canvas and Chart, but that is not necessary for Image. If no width and height are specified for an image, the width and height are obtained from the image file.

* object-area-size = width\_and\_height-size
* cell-area-size = max (grid-size, object-area-size + padding)

##### 2.3.1.4. Row, Column

For Row and Column, width and height are minimum values and set on the cell area. If the objects contained in the Row and Column are bigger than the specified size, the cell area is expanded. On a Column it is only possible to specify width, not height. On a Row it is only possible to specify height, not width.
Note that Row and Column do not have any object area.

* cell-area-size = max (grid-size, specified-size, included-objects-size)

#### [2.3.2. align, valign](#id20)

align and valign are cell attributes and specify horizontal and vertical alignment of the object area inside the cell.

##### 2.3.2.1. Text

For a Text object, the align attribute aligns both the object area inside the cell but also the text that flows in the object area.

##### 2.3.2.2. Isolate, Chart, Canvas, Image

The attribute aligns the object area inside the cell area.

##### 2.3.2.3. Row, Column

align and valign cannot be applied to Row and Column since these objects do not have an object area.

#### [2.3.3. colspan, rowspan](#id21)

colspan and rowspan are cell attributes, and specify how many columns or rows in the grid a cell should span.
Note that all objects have a colspan and a rowspan even if a value has not been explicitly specified. The default value for all objects is a colspan and rowspan of 1.

##### 2.3.3.1. Isolate, Image, Canvas, Chart, Text

If a colspan/rowspan value has been explicitly specified, this will be used as actual value. If no value has been explicitly specified, the actual value is adjusted to fit the surrounding grid.

##### 2.3.3.2. Column

It is only possible to set colspan, not rowspan, on a Column. The value of the colspan for a Column is:
\* colspan = max(1, max (child-colspan), specified-colspan).

If the column has no explicitly specified colspan, the colspan of the column is adjusted to the actual value received from the enclosing objects. If colspan has explicitly been specified, the colspan value can not be modified by the enclosing object. It is however still a minimum value and if the objects contained in the Column has a greater value than the on the Column specified value, the colspan is set to colspan of the contained objects.

It is not possible to specify rowspan for a Column. The default rowspan value for the Column is therefore decided by:

* rowspan = max (1, sum(child-rowspan), grid-rowspan)

If the rowspan available in the grid is larger than the column’s own span, the column tries to adjust the rowspan of the last object in the column. If the last object in the column cannot be adjusted, an empty object is added after the last object in the column.

##### 2.3.3.3. Row

Row behaves analogously with Column, but with colspan instead of rowspan.

#### [2.3.4. Empty cells](#id22)

A Row or Column is always rectangular. Sometimes it is necessary to fill out its space in the grid by adding an empty cell to the cell of the enclosing object. This means that a border set on the enclosing object will include the empty cell.
For example, if the last Text object inside a row has a specified colspan of 1 and if the row needs the colspan to be increased, an empty cell is added to the right of the object.

#### [2.3.5. padding](#id23)

padding is a cell property and defines the minimum space between the object area and the cell area. The size of the object area can never be changed by the cell. The padding therefore only affects the size of the cell. The cell area is expanded if padding is set.
•

cell\_size = max (grid-size, object-area-size + padding)

#### [2.3.6. font, colour](#id24)

font and colour are object attributes. Colour sets the foreground colour (the colour of text and lines).

* For Text, font and colour are set on the text in the object.
* For Canvas and Chart, font and colour are set as default values for the drawing.
* For containers (Isolate, Row and Column), font and colour are inherited by the objects in the container.

#### [2.3.7. background](#id25)

background is a cell attribute and defines the colour of the cell area. It is not possible to set a background on the object only.

#### [2.3.8. border](#id26)

`border` is a cell attribute and defines the border around the cell. There are three different functions for creating borders:

border()
:   Allows the report writer to define the border for any side of the cell. For Row and Column objects, you can also set the border for cells inside these objects.

border\_frame()
:   sets a border around the cell.

border\_all()
:   Sets a border around the cell, and for Row and Column objects around the cells contained in the object.

#### [2.3.9. action, link, url](#id27)

The action, link, and url attributes are all object attributes. They are only valid for Text, Image, Canvas and Chart.

### [2.4. Page definition](#id28)

The concept of a page differs between output formats. PDF is a paged medium with a well-defined concept of discrete pages of a certain size. HTML viewed in a browser is a continuous medium without clearly defined page sizes, breaks, etc. However, pagination aspects do apply to HTML output when the page is printed.

For plain text output, the page concept is not applicable.

#### [2.4.1. Margins](#id29)

The default page margins for both PDF and HTML are (in pixels, left to bottom, clockwise): 42, 36, 36, 36. Other margins can be set using the padding() function.

#### [2.4.2. Page width](#id30)

The Report.page\_width() method returns the width of the page minus margins.

#### [2.4.3. Paper size](#id31)

The Report.setpaper() method is use to set paper orientation and size.

#### [2.4.4. PDF page breaks](#id32)

In PDF output, three Column methods for controlling page breaks are available: `newpage()`,
`page()`, and `page0()`.

`newpage()`
:   Hard page break. A page break is always added at this place in the column.

`page()`
:   Soft page break with high priority.

`page0()`
:   Soft page break with low priority.

#### [2.4.5. HTML page breaks](#id33)

When printing HTML output, only the `newpage()` method applies.
