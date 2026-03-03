## CSV reports


The `CSVReport` class makes it possible to create reports that output tabular
data using *comma/character separated values*. This can be useful when you need to copy
report data to Excel and other spreadsheet programs.

#### 3.17.1. Example

```
import carmensystems.publisher.api as p

class Report(p.CSVReport):

    def __init__(self, *args, **kwargs):
        super(Report, self).__init__(*args, **kwargs)

    def create(self):
        self.data.append(["Test of comma separated file", "#1"])
        self.data.append(["Integers:", 1, 2, 3, 4])
```

### Example