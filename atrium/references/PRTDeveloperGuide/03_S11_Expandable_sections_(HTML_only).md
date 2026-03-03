## Expandable sections (HTML only)


By specifying a box as expandable, the contents of the box is initially hidden. Clicking on the header
toggles display of the contents (the body). Below are two examples.

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        self.set(border=p.border_all())
        self.add("Simple expandable example")

        col = p.Column()
        self.add(p.Expandable("TOGGLE", col))
        col.add("Row 1")
        col.add("Row 2")
        col.add("Row 3")
```

Output in collapsed and expanded state:

![_images/collapsed1.png](_images/collapsed1.png)
![_images/expanded1.png](_images/expanded1.png)

```
import carmensystems.publisher.api as p

### A table with two expandable rows, one expandable column,
### and one regular row

class Report(p.Report):
    def create(self):
        self.set(border=p.border_all())
        self.add("Expandable test: table")
        self.add(p.Row(p.Column(p.Expandable("Expand",
                                             p.Row(p.Column(11,21),
                                                   p.Column(12,22),
                                                   rowspan=2)),
                                p.Row(31,32)),
                       p.Expandable("Expand",
                                    p.Column(13,23,33),
                                    valign=p.TOP, rowspan=3)))

        self.add(p.Expandable("Expand",
                              p.Row(41,42,43), colspan=3))
```

Output in collapsed and expanded state:

![_images/collapsed2.png](_images/collapsed2.png)
![_images/expanded2.png](_images/expanded2.png)