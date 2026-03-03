## Pattern


Patterns are objects used to fill polygons with a pattern.

The `bigC` function draws a figure resembling a capital letter C. In the `Pict` class,
a pattern that fills the inside of the figure is added using the `fill` property. The pattern consists of:

* red horizontal lines, slanted 45°, separated by 8 pixels
* green horizontal lines, slanted -45°, separated by 8 pixels

```
import carmensystems.publisher.api as p

def bigC(gc, x0, y0, scale, fill):
    moves = [(-1,1),(0,3),(1,1),(3,0),(1,-1),(0,-1),
             (-1,0),
             (-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),
             (1,0),
             (0,-1),(-1,-1),(-3,0)]
    coords = [(x0, y0)] + [p.Move(scale*x, scale*y) for (x,y)
                            in moves]
    gc.path(coords, fill=fill)

class Pict(p.Canvas):
    def draw(self, gc):
        pattern = p.Pattern()
        pattern.hline(8, 1, colour='#ff0000')
        pattern.hline(8, -1, colour='#00ff00')
        bigC(gc, 50, 50, 20, pattern)

class Report(p.Report):
    def create(self):
        self.add("An example picture with a pattern")
        self.add(Pict(200,200))
```

Output:

![_images/pattern.png](_images/pattern.png)