## Cross-references


A `Crossref` creates a cross-reference or an internal link to a page number or to a
named component elsewhere in the report. It is used as part of the text in a `Text`
box. By default this creates an internal link, where the link text is the number of the
page where you will find the referred component. When referring to one of the special
names `current_page` or `last_page`, the result is just a page number; no link is created.

The following example demonstrates the use of Header, Footer and Crossref. The output (in
PDF format) is a two-page report with different headers and footers on each page. In HTML
format, the report will be on two separate pages when it is printed.

The report also shows how `Report.setpaper()` and `Report.newpage()` can be used.

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        hdrfont = p.Font(size=20)
        ftrfont = p.Font(size=12)
        self.setpaper(p.LANDSCAPE, p.C5)

        for i in range(1,3):
            header = p.Header(p.Text("Header %s" %i,
                                     font=hdrfont))

            footer = p.Footer(p.Text("Footer %s (Page "%i,
                                   p.Crossref('current_page'),' of ',
                                   p.Crossref('last_page'), ')',
                                   font=ftrfont))

            table = p.Column(p.Row("first","second","third"),
                             p.Row(p.Text("Span two columns",
                                          colspan=2),
                                   "one column"),
                             p.Row(p.Column("first","second","third"),
                                   p.Column(p.Text("Span two rows",
                                                   rowspan=2),
                                            "one row"),
                                   p.Text("")),
                             border=p.border_all(1))

            self.add(header)
            self.add(footer)
            self.add(table)

            # One page break
            if i < 2:
                self.newpage()
```

Output (two-page PDF):

[![_images/Crossref-1a.png](_images/Crossref-1a.png)](_images/Crossref-1a.png)
[![_images/Crossref-2a.png](_images/Crossref-2a.png)](_images/Crossref-2a.png)