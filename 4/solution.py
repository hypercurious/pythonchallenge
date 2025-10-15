#!/usr/bin/env python3
import os, re
import requests

def get_next_nothing(nothing_line):
    next_nothing = re.search(r'(\d+)$', nothing_line).group(1)
    next_nothing_response = requests.get(
        url='http://www.pythonchallenge.com/pc/def/linkedlist.php',
        params={
            'nothing': next_nothing
        },
        timeout=10,
    )
    print(next_nothing_response.text)
    with open('output.txt', 'a') as f:
        f.write('\n'+next_nothing_response.text)
    get_next_nothing(next_nothing_response.text)

try:
    if not os.path.exists('output.txt'):
        with open('output.txt', 'w') as f:
            pass
        first_nothing = "# you can find this number by clicking the picture 12345"
    else:
        with open('output.txt', 'r') as f:
            nothing_logs = f.read()
        first_nothing = nothing_logs.split()[-1]
    get_next_nothing(first_nothing)
except Exception as e:
    print(e)
except:
    print('unt')

