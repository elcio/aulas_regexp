#!/usr/bin/env python

import sys
import re

text = open(sys.argv[2]).read()
repls = eval(open(sys.argv[1]).read())

for a, b in repls:
    text = re.sub(a, b, text)

print(text)
