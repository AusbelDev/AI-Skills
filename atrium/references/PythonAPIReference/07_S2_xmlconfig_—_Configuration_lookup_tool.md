## xmlconfig — Configuration lookup tool


The command line interface allows for higher level lookups of the configuration;
that is, lookups combined with several queries and default behaviours.

#### Synopsis

```
xmlconfig [options][<configfile>] <command | query1 [query2 [...]]>
```

If the first argument (`<configfile>`) does not end with ‘.xml’, the default configuration file `${CARMSYS}/etc/system_config.xml` is used.

#### Options

|  |  |
| --- | --- |
| `-d` | enable debugging printouts (must be first argument; repeat to increase debug level) |
| `-h, --help` | display help text (no configfile is needed) |
| `-v, --version` | print component version (no configfile is needed) |

#### Commands

|  |  |
| --- | --- |
| `--list` | list all properties, without variable expansion |
| `--xml` | dump the XML tree after all files are included |
| `--all` | list all xpaths |
| `--srv` | list all services in all process groups.  Note that applications only check for services within their own process group. |
| `--url <service [host]>` | |
|  | locate a service [on host <host>] |
| `--port <service [host]>` | |
|  | shorthand to find the port number for service[@host] |

#### Queries

An “xpath” query has this basic syntax:

```
xpath | */xpath | *[n]@attr | *
```

Examples:

```
some/path,
some/path[3]
some/path@someattr
some/path@*
some/*/path[2]@*
*/*[1]/@*
```

### Synopsis

### Options

### Commands

### Queries