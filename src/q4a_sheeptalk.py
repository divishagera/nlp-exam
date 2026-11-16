# 4a: Write a python program that uses regular expressions to simulate a Finite
# State Automata(FSA) for recognizing sheeptalk strings.

import re


def is_sheeptalk(text):
  # Recognizes 'b' followed by two or more 'a's and ending with '!'
  pattern = r"^ba{2,}!$"
  return bool(re.match(pattern, text))


if __name__ == "__main__":
  user_input = input(
      "Enter a string to test (or press Enter to run sample tests): "
  ).strip()
  if user_input:
    print(f"'{user_input}' -> {is_sheeptalk(user_input)}")
  else:
    samples = ["baa!", "baaa!", "ba!", "baaaa!", "baa!!", "b!"]
    for s in samples:
      print(f"{s:<8} -> {is_sheeptalk(s)}")
