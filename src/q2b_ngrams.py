# 2b: Write a program to implement N-Gram Model from the given text, excluding
# the stop words.

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

for resource in ["punkt", "punkt_tab", "stopwords"]:
  nltk.download(resource, quiet=True)


def build_ngram_model(text, n):
  stop_words = set(stopwords.words("english"))
  tokens = [
      token.lower()
      for token in word_tokenize(text)
      if re.match(r"^[a-zA-Z]+$", token)
      and token.lower() not in stop_words
  ]
  return list(ngrams(tokens, n))


if __name__ == "__main__":
  text = input("Enter the input text: ")
  n = int(input("Enter N for N-gram (e.g., 2 for bigram, 3 for trigram): "))

  result_ngrams = build_ngram_model(text, n)
  print(f"{n}-Grams (excluding stop words):")
  print(result_ngrams)
