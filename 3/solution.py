#!/usr/bin/env python3
import re
from sys import argv

try:
    input_text = argv[1] if len(argv)>1 else open('input.txt', 'r').read()
except Exception:
    input_text = argv[-1]

result = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", input_text)

print(''.join(result))
