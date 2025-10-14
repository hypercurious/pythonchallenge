#!/usr/bin/env python3
from sys import argv

try:
    input_text = argv[1] if len(argv)>1 else open('input.txt', 'r').read()
except Exception:
    input_text = argv[-1]

# !!! very slow solution !!!
#result = sorted(list(input_text), key=input_text.count)[:15]
#print(''.join(result))

result = filter(None, map(lambda x: x if x.isalpha() else None, input_text))
print(''.join(result))

