# 2b: Write a program to implement N-Gram Model from the given text, excluding
# the stop words.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

text = input("Enter text: ")
n = int(input("Enter N for N-gram (e.g., 2 for bigram): "))

stop_words = set(stopwords.words("english"))
words = [
    w.lower()
    for w in word_tokenize(text)
    if w.isalpha() and w.lower() not in stop_words
]

print(f"{n}-grams:", list(ngrams(words, n)))
