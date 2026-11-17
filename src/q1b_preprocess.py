# 1b: Write a program to Perform Preprocessing (Tokenization, Stop Word Removal
# and Stemming) of Text.

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

text = input("Enter text to preprocess: ")

tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words("english"))
filtered = [w for w in tokens if w.isalnum() and w not in stop_words]

stemmer = PorterStemmer()
stemmed = [stemmer.stem(w) for w in filtered]

print("Tokens:", tokens)
print("After Stop Word Removal:", filtered)
print("After Stemming:", stemmed)
