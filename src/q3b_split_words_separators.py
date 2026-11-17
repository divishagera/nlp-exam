# 3b: Write a Python program to split a string of words separated by commas and
# spaces into two lists, words and separators.
# Sample input: "The colors in my studyroom are blue, green, and yellow."

import re


def split_words(text):
  tokens = re.split(r"([ ,]+)", text)
  words = tokens[0::2]
  separators = tokens[1::2]
  return words, separators


text = "me, you, him, her, they, so"
words, separators = split_words(text)

print("words", words)
print("seperators", separators)
