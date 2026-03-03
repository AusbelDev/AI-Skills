## A simple tabular report


The table in this example is organized as a column of rows. If a row of columns is preferred, change Column to Row and vice versa:

```
import carmensystems.publisher.api as p

cp_data = [('ATl',10), ('CVG',5), ('LAX',4)]

class Report(p.Report):
     def create(self):
         table = p.Column()
         for (airport,x) in cp_data:
             table.add(p.Row(airport,x))
         self.add(table)
```

Borders can be added by using `p.border` in suitable places:

```
import carmensystems.publisher.api as p

cp_data = [('ATl', 10), ('CVG', 5), ('LAX', 4)]

class Report(p.Report):
    def create(self):
        table = p.Column()
        for (airport, x) in cp_data:
            table.add(p.Row(airport, x,
                            border=p.border(bottom=1)))
        self.add(table)
```

The `add()` method implicitly wraps everything that is not a box with `Text`. Text
properties that are given in a `Row` or `Column` are inherited by all boxes that are placed in
the row/column.

Advanced tables are created by nesting rows and columns:

```
import carmensystems.publisher.api as p

cp_data = [('ATL', 10, 12), ('CVG', 5, 7), ('LAX', 4, 4)]

class Report(p.Report):
    def create(self):
        table = self.add(p.Column())

        table.add(p.Row(p.Text("Airport", valign=p.TOP),
                        p.Column(p.Text("CP",
                                        align=p.CENTER,
                                        valign=p.TOP),
                                 p.Row("data","max")),
                        font=p.Font(weight=p.BOLD)))

        for (airport,x,m) in cp_data:
            table.add(p.Row(airport,x,m))
```