#!/usr/bin/python3
"""takes an argument 2 strings"""
import os
import sys

if len(sys.argv) < 2:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    exit(1)

if not os.path.exists(sys.argv[1]):
    sys.stderr.write("Missing " + sys.argv[1] + "\n")
    exit(1)

exit(0)
