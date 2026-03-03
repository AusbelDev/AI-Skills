## Column headers and footers


Column headers and footers are added to columns similar to the way you can add running
headers and footers on a report. These boxes are added using the `add_header()` and
`add_footer()` methods. If a page break is introduced in the column, column headers and
footers are repeated on the next page.

Column headers and footers cannot be added to columns that reside in rows. The following
code creates a 70-row column with header and footer.

```
import carmensystems.publisher.api as p

class Report(p.Report):
    def create(self):
        col = p.Column(border=p.border_all(1))

        col_header = p.Row("First","Second","Third",
                          border=p.border_all(1),
                          background="#DDDDEE")

        col_footer = p.Row("First","Second","Third",
                          border=p.border_all(1),
                          background="#DDDDEE")

        col.add_header(col_header)
        col.add_footer(col_footer)

        for i in range(70):
            col.add(p.Row(i, i+1, i+2))
            col.page()

        self.add(p.Header("Report header"))
        self.add(col)
```

Note

Using `add_header()` or `add_footer()` on the `Report` itself
overrides any previously added `Header` or `Footer` boxes.