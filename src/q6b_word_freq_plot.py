# 6b: Plot Graph of Most Frequent Words Without Stop Words and Punctuation

import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

sentence = input("Enter a sentence: ")
words = word_tokenize(sentence)
print(len(words))

stop_words = set(stopwords.words("english"))
print(len(stop_words))

word_no_pun = []
for w in words:
    if w.isalpha():
        word_no_pun.append(w.lower())

print(word_no_pun)
print(len(word_no_pun))

clean_words = []
for w in word_no_pun:
    if w not in stop_words:
        clean_words.append(w)

print(clean_words)
print(len(clean_words))

fdist = FreqDist(clean_words)
print(fdist.most_common(10))
fdist.plot()
plt.show()
