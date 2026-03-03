## Canvas drawings


A canvas is a user-defined drawing area. The actual drawing is done in the `draw()`
method which takes a `Graphic` object as argument. A `Graphic` object cannot
be created by the user; it is simply passed to the method by the framework.

The following methods are available on `Graphic` objects:

`get_coordinates(self)`
:   Gets the coordinates.

`coordinates(self, minx, miny, maxx, maxy)`
:   Sets the coordinates.

`path(self, coords, width=1, colour='#000000', close=False, fill=None, link=None, action=None)`
:   Draws a line or polygon defined by the points listed in `coords`.

`image(self, x0, y0, path, align=None, valign=None, link=None, action=None, width=None, height=None)`
:   Inserts an image at the given position.

`image_size(self, path)`
:   Gets the amount of space needed by this image.

`text(self, x0, y0, *texts, **properties)`
:   Draws text at the given position.

`text_size(self, *texts, **properties)`
:   Gets the amount of space needed by this text.

`rectangle(self, x0, y0, width, height, colour=None, fill=None, linewidth=1, link=None, action=None, align=None, valign=None)`
:   Draws a rectangle starting at `(x0,y0)`.

`marker(self, x0, y0, mark, colour='#000000', link=None, action=None)`
:   Draws a marker, as specified by the mark argument.

#### 3.6.1. Drawing simple shapes

The code in the following example draws a simple figure. First it draws one triangle,
fills it with the `#00ff00` colour (green), moves to the middle of the long edge, and
writes text1 in blue. Then it draws another triangle, fills it with `#0000ff` colour
(blue), moves to the middle of the long edge, and writes text2 in green.

```
import carmensystems.publisher.api as p

class Pict(p.Canvas):
    def draw(self,gc):
        gc.path([(0,0),(100,50),(100,100),(0,0)],
                fill='#00ff00')
        gc.text(50,50, "text1", colour="#0000ff")
        gc.path([(100,50),(200,0),(100,100), (100,50)],
                fill='#0000ff')
        gc.text(150,50, "text2", colour="#00ff00")

class Report(p.Report):
    def create(self):
        self.add(Pict(200,100))
```

Output:

![_images/Canvas.png](_images/Canvas.png)

#### 3.6.2. Rotated text with markers

The following example illustrates the use of markers and rotated text. The markers are
coloured using the Nordic Light palette.

```
import carmensystems.publisher.api as p
import carmensystems.publisher.nordiclight as N

nordic = N.palette()

class Pict(p.Canvas):
    def draw(self,gc):
        gc.text(30, 150, "Marker 1",
                rotate=0,
                valign=p.CENTER,
                align=p.CENTER)
        gc.marker(30, 155,
                  p.Marker('x', colour=nordic.Red,
                           linewidth=3))

        gc.text(80, 150, "Marker 2",
                rotate=90,
                valign=p.CENTER,
                align=p.CENTER)
        gc.marker(75, 150,
                  p.Marker('+', colour=nordic.Green,
                           linewidth=3))

        gc.text(130, 150, "Marker 3",
                rotate=180,
                valign=p.CENTER,
                align=p.CENTER)
        gc.marker(130,145,
                  p.Marker('d', colour=nordic.Orange,
                           linewidth=3))

        gc.text(180, 150, "Marker 4",
                rotate=270,
                valign=p.CENTER,
                align=p.CENTER)
        gc.marker(170, 150,
                  p.Marker('<', colour=nordic.Blue,
                           linewidth=3))

class Report(p.Report):
    def create(self):
        self.add("A marker/rotate/nordic light example")
        self.add(Pict(200, 200))
```

Output:

![_images/marker.png](_images/marker.png)

### Drawing simple shapes

### Rotated text with markers