#!/usr/bin/env python3
"""Show where an IOService runs in every system layout of a $CARMUSR.

Usage: service_placement.py <service-name> [<carmusr>]

<service-name> is the activation config name, e.g. RosterStateOutput_5_ODH_plainxml
(the file usr/etc/programs/ioservices/datafeeds/<service-name>.xml). <carmusr> defaults
to $CARMUSR.

For each layout (etc/programs/sysmond/<SERVICE_CONFIG_TYPE>.xml) it prints the nodes that
start an IOServer process including the service, how many such processes each node starts,
and the worker pool from etc/programs/ioservices/<SERVICE_CONFIG_TYPE>.xml. It flags layouts
where the service does not run, runs in more than one process, or has no pool file, and
exits 1 if any layout is flagged. More than one instance is normal for services that may
scale out; it is only wrong for a service that must run once (ordering, single consumer).
"""
import glob
import os
import re
import sys


def strip_comments(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    service = argv[1]
    carmusr = argv[2] if len(argv) > 2 else os.environ.get("CARMUSR")
    if not carmusr:
        sys.exit("No <carmusr> given and $CARMUSR is not set")
    programs = os.path.join(carmusr, "etc", "programs")

    # Process name -> whether its process file includes the service.
    include = re.compile(r'<include\s+href="[^"]*/{}\.xml"'.format(re.escape(service)))
    hosts = {}
    for path in glob.glob(os.path.join(programs, "ioserver*.xml")):
        text = strip_comments(open(path, encoding="latin-1").read())
        for name in re.findall(r'<process\s+name="([^"]+)"', text):
            hosts[name] = bool(include.search(text))
    hosting = sorted(name for name, has in hosts.items() if has)
    print("Processes including {}: {}".format(service, ", ".join(hosting) or "none"))

    ok = True
    layouts = sorted(p for p in glob.glob(os.path.join(programs, "sysmond", "*.xml"))
                     if not p.endswith("_ioservice_settings.xml"))
    for path in layouts:
        layout = os.path.basename(path)[:-len(".xml")]
        text = strip_comments(open(path, encoding="latin-1").read())
        nodes = []
        for block in re.split(r'<process\s+name="', text)[1:]:
            node = block.split('"', 1)[0]
            started = re.findall(r"<start>\s*([\w.-]+)\s*</start>", block)
            count = sum(1 for p in started if hosts.get(p))
            if count:
                nodes.append((node, count))
        instances = sum(count for _, count in nodes)

        pool_file = os.path.join(programs, "ioservices", layout + ".xml")
        if os.path.exists(pool_file):
            match = re.search(r"<{0}>\s*(\d+)\s*</{0}>".format(re.escape(service)),
                              strip_comments(open(pool_file, encoding="latin-1").read()))
            pool = match.group(1) if match else "not set"
        else:
            pool = "no pool file"

        where = ", ".join("{} x{}".format(n, c) for n, c in nodes) or "NOT RUN"
        flags = []
        if instances == 0:
            flags.append("service does not run")
        elif instances > 1:
            flags.append("{} instances (wrong only if it must run once)".format(instances))
        if pool == "no pool file":
            flags.append("missing {}".format(os.path.relpath(pool_file, carmusr)))
        if flags:
            ok = False
        print("{:<20} {:<40} workers: {:<13} {}".format(
            layout, where, pool, "<-- " + "; ".join(flags) if flags else ""))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
