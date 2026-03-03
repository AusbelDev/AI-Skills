## A simple chart


The data in the simple table example can be used to create a simple chart:

```
import carmensystems.publisher.api as p

cp_data = [ ('ATL',10), ('CVG',5), ('LAX',4) ]

class Report(p.Report):

    def create(self):
        ser = p.Series(cp_data,
                       graph=p.Bar(width=0.5))

        self.add(p.Chart(200,200, ser))
```

This is how it is rendered:

![_images/chart1.png](_images/chart1.png)

The `Chart` class takes one or more `Series` and creates a chart in a box. The size of the box
must be explicitly given in number of pixels. The `Series` class can be used to add
properties to the data using a list of key-value pairs (no properties are used in the
example above).

If you intend to use multiple series, then it is a good idea to make it possible to
distinguish them. There are several useful properties for `Series` and combinations of
`Series`, for example:

`colour`
:   Set the colour of the data set or text (in #RRGGBB format).

`graph`
:   Specifies a Graph object. The following graph types exist: Area, Bar, Limit, Line, Marker.

`legends`
:   Gives a name to a series in the form of `(label, colour)` 2-tuples, to be used in legends.

Series can be combined with the `Combine` class. How they are combined is determined by properties. For example:

`width`
:   The part of the horizontal space available that is used for Limit and Bar graphs (1.0 means all available space).

`on_top`
:   A boolean value specifying whether data sets should be placed on top of each other.

The `Chart` class determines the range of keys and values from the given data, but
it is also possible to set the recommended minimum and maximum values by setting the
`xaxis_limits` and `yaxis_limits` properties. These properties set minimum and/or
maximum values for the x/y-axis.The limits might be rounded by the system to make it
easier to place the tick marks.

The following is a more advanced chart example using some properties:

```
import carmensystems.publisher.api as p

cp_data = [ ('ATL',10,12), ('CVG',5,7), ('LAX',4,4) ]

class Report(p.Report):
    def create(self):
        ser1 = p.Series([(k,d) for (k,d,m) in
                         cp_data],
                        label='CO',
                        graph=p.Bar(fill="#00ff00",
                                    width=0.5))

        ser2 = p.Series([(k,m) for (k,d,m) in
                         cp_data],
                        label='CO max',
                        graph=p.Limit(colour="#000000"))

        chart = p.Chart(200,200,
                        p.Combine(ser1, ser2,
                                  on_top=False,
                                  yaxis_limits=(0,None)))

        self.add(chart)
```

Output:

![_images/chart2.png](_images/chart2.png)