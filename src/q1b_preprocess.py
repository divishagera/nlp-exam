# 1b: Write a program to Perform Preprocessing (Tokenization, Stop Word Removal
# and Stemming) of Text.

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

for resource in ["punkt", "punkt_tab", "stopwords"]:
  nltk.download(resource, quiet=True)


def preprocess_text(text):
  # 1. Tokenization
  tokens = word_tokenize(text.lower())

  # 2. Stop word removal (and keeping word tokens only)
  stop_words = set(stopwords.words("english"))
  filtered_tokens = [
      token
      for token in tokens
      if token not in stop_words and re.match(r"^[a-z0-9]+$", token)
  ]

  # 3. Stemming
  stemmer = PorterStemmer()
  stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

  return tokens, filtered_tokens, stemmed_tokens


if __name__ == "__main__":
  sample_text = (
      "Natural Language Processing helps computers analyze and understand human"
      " languages."
  )
  tokens, without_stopwords, stemmed = preprocess_text(sample_text)

  print("Tokens:", tokens)
  print("After Stop Word Removal:", without_stopwords)
  print("After Stemming:", stemmed)
