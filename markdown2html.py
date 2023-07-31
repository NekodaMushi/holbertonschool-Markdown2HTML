#!/usr/bin/python3

"""function parsing Headings Markdown syntax for generating HTML"""

import os
import sys

if __name__ == "__main__":
    import os
    import sys

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit(1)

    with open(sys.argv[1], "r") as f_mark:
        lines = f_mark.readlines()

    html_content = []
    for line in lines:
        if line.startswith("#"):
            Hlevel = line.count("#")
            textContent = line[Hlevel:].strip()
            html_content.append(f"<h{Hlevel}>{textContent}</h{Hlevel}>")

    html_version = "\n".join(html_content)

    with open(sys.argv[2], "w") as f_html:
        f_html.write(html_version)

    exit(0)
