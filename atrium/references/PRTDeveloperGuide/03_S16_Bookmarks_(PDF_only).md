## Bookmarks (PDF only)


Bookmarks can be added to components using the bookmark property. Example:

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        self.add(p.Text("Header text 1",
                        bookmark=p.bookmark("Bookmark 1")))
        self.add(p.Text("Header text 2",
                        bookmark=p.bookmark("Bookmark 2",
                                            level=2)))
```