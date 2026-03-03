## Links (HTML only)


The `link()` and `url()` functions can be used to create hyperlinks to other reports or web pages. Both links and URLs are given as values to the keyword argument link:

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        myurl = p.url("http://www.jeppesen.com")
        self.add(p.Text("Link to Jeppesen"))
        self.add(p.Text("Click here", link=myurl))
```

Note

The `link()` function is currently not supported in Atrium.