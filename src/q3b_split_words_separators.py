# 3b: Write a Python program to split a string of words separated by commas and
# spaces into two lists, words and separators.
# Sample input: "The colors in my studyroom are blue, green, and yellow."

import re


def split_words_and_separators(text):
  # Separators consist of commas with optional spaces, or whitespace sequences
  tokens = re.split(r"(,\s*|\s+)", text)
  words = [t for i, t in enumerate(tokens) if i % 2 == 0 and t != ""]
  separators = [t for i, t in enumerate(tokens) if i % 2 == 1 and t != ""]
  return [words, separators]


if __name__ == "__main__":
  default_text = "The colors in my studyroom are blue, green, and yellow."
  user_text = input(
      "Enter text separated by commas and spaces (or press Enter for sample"
      " input): "
  ).strip()

  text = user_text if user_text else default_text
  words, separators = split_words_and_separators(text)

  print("Words:", words)
  print("Separators:", separators)
  print("Combined Output:", [words, separators])
