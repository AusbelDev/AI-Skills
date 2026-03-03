## Images


Static images (JPEG only) can be inserted using the `Image` class. The paths to the
image files are assumed to be relative to `$CARMSYS/images` or `$CARMUSR/images`.

Note

Images are embedded in the reports so unnecessarily large images should be avoided. A general recommendation is to keep the total size of images included in reports that are created/stored in large numbers below 10Kb.

Example:

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        self.add(p.Image('jepplogo.jpg', width=100))
```