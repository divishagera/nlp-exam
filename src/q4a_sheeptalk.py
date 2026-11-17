# 4a: Write a python program that uses regular expressions to simulate a Finite
# State Automata(FSA) for recognizing sheeptalk strings.

import re

def is_sheeptalk(string):
    # ^ start, ba fixed state, min & max req, $ end
    pattern = r"^ba{2,3}!$"
    return bool(re.match(pattern, string))

test_strings = ["baa!", "baaa!", "ba!", "baa!!", "baa!!", "b!", "baaaa!"]

for s in test_strings:
    print(f"'{s}' : {is_sheeptalk(s)}")
