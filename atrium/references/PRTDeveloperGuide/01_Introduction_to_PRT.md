# Introduction to PRT


Python Report Toolkit (PRT) is a toolkit for report generation. The reports are written in
Python, using constructs defined in the `carmensystems.publisher.api` API. The API provides classes and functions
for layout of complex tables and charts using multiple fonts, styles, alignments,
graphics, etc. The currently supported output formats are HTML, PDF and CSV.

Report generation is normally started from your graphical user interface. The PRT environment can be used
stand-alone, but it is often used together with the Rave Python API, the API
that provides access to Rave data (`carmensystems.rave.api`).

[Link to the API reference documentation](../com.jeppesen.jcms.cms.help.python/index.html#rave-publisher-prt).

### 1.1. Class overview

The following figure contains an overview of the classes in `carmensystems.publisher.api`.

![_images/PRT_Classes.png](_images/PRT_Classes.png)

### 1.2. Report types

The currently supported output formats are:

* HTML
* PDF
* CSV

### 1.3. Generating and viewing reports from the UI

Detailed instructions are found in
[Client Configuration Developer Guide, chapter “Adding a report in PWS”](../doc.atrium.configuration/Patterns/report.html).

### 1.4. Using a command line script

Reports can be created from the command line with the `$CARMSYS/bin/publisher` script.

#### 1.4.1. Synopsis

```
publisher [options] report_module
```

The options are:

|  |  |
| --- | --- |
| `--format <format>, -f <format>` | |
|  | Set output format. <format> is either pdf, html, or txt. The default is pdf. |
| `--help, -h` | Print this help. |
| `--output <output>, -o <output>` | |
|  | Save result to file <output>.  If no extension is given, it is added according to format (.pdf, .html, or .txt). Any additional files, such as image files for HTML, are stored in the directory <output>\_files.  If no output file is specified, the output is put in the current directory, with the report module name as file name. |
| `--param nameval, -p nameval` | |
|  | Pass a named parameter to the report (where `nameval` should be written as `name=val`). |
| `--viewer <app>, -v <app>` | |
|  | View the generated file by calling <app> <output>. The viewer program can be, for example, Firefox or xpdf. |

Relevant environment variables must be set when invoking the publisher script: `PATH`, `CARMSYS`,
`CARMUSR`, and `CARMTMP`. The variables defined in `$CARMSYS/CONFIG` must also be available to the shell.

### 1.5. Using the generateReport function

The `carmensystems.publisher.api` module contains the `generateReport()` function,
which can be used to create reports from a Python program.

#### 1.5.1. Synopsis

```
generateReport(source, outputfile, format=PDF, reportparams={} [, context])
```

Render a report in the specified format and save it in `outputfile`. The report instance is then
deleted.

#### 1.5.2. Arguments

`source`
:   The module name of the report.

`outputfile`
:   Destination file. If no extension is given, it is added according to format (.pdf or
    .html). Any additional files, such as image files for HTML, are stored in the directory
    `<outputfile>_files`.

`format`
:   Either PDF, HTML or TXT (these are module constants)

`reportparams`
:   Additional parameters to the report, passed as a dictionary mapping parameter names to
    values. Both names and values must be strings. In the report, a parameter value can be
    retrieved via the `Report.arg(paramname)()` method.

`context`
:   Optional context locator object to use in the report. When the report is finished it
    returns the full path to the generated file.

### 1.6. General guidelines for images

Images in reports are embedded so unnecessarily large images should be avoided. A general
recommendation is to keep the size of (all) images included in reports that are created/stored
in large numbers below 10Kb.
