## The Hello world report


Below is a minimal report example that only displays the text “Hello world”:

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        self.add("Hello world")
```

The module imports the PRT API. Using the `import XXX as Y` style is preferred. The `from XXX import *` style should not be used.

The report class can be called `Report` or have the same name as the report module, and
it must inherit from `Report`. The `create()` method creates the report. In this case it
just adds the text “Hello world” using the `add()` method. This is all that is needed to
create a report with only a text string.

#### 3.1.1. Changing appearance

You can change the appearance of the text by using properties that are specified as keyword arguments. For
example, you can make the text bold by writing:

```
self.add(P.Text("Hello world",
                font=p.Font(weight=p.BOLD)))
```

Note

The text string must be the first argument.
You can add more than one property, for example:

```
self.add("Hello world", font=p.Font(weight=p.BOLD,
                                    style=p.ITALIC))
```

There are several other properties that change the appearance of the text. Some properties do not change the text itself but only the box that the text is enclosed in. Some of these are:

border
:   Draws a border around the component, using the functions border(), border\_frame() or border\_all().

width
:   Sets the width of the box.

height
:   Sets the height of the box.

align
:   Specifies how the text is placed horizontally in the box, where valid values are the module constants LEFT, CENTER, and RIGHT.

valign
:   How the text is placed vertically in the box. Valid values are the module constants TOP, CENTER, and BOTTOM.

Below is a slightly more complicated property example:

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        self.add(p.Text("Hello world",
                        border=p.border(top=1, bottom=1),
                        font=p.Font(weight=p.BOLD),
                        width=80))
```

The above example creates a report row with “Hello world” in bold, with a line above and
below the text. If no size is given, then the size of the box is calculated by PRT. This
is the preferred method and works best for reports that can be output in several formats,
for example HTML and PDF.

### Changing appearance