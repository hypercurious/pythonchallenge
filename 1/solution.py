#!/usr/bin/env python3
import string
from sys import argv

try:
    input_text = argv[1] if len(argv)>1 else open('input', 'r').read()
except Exception:
    input_text = argv[-1]

l = string.ascii_lowercase
mapping = dict(zip(l,l[2:]+l[:2]))
result = map(lambda x: mapping.get(x, x), input_text)

print(''.join(result))
