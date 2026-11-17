# 2b: Write a program to implement N-Gram Model from the given text, excluding
# the stop words.

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

def generate_ngrams(text, n=2):
    stop_words = set(stopwords.words("english"))
    words = [word for word in text.lower().split() if word not in stop_words]
    print("words after removing stopwords:", words)
    temp = zip(*[words[i:] for i in range(0, n)])
    ans = [" ".join(ngram_tuple) for ngram_tuple in temp]
    return ans

user_text = input("Enter text: ").strip()
if not user_text:
    user_text = "The sun rises in the east and sets in the west"
n_val = int(input("Enter N for N-gram (e.g., 2): ") or 2)

result = generate_ngrams(user_text, n_val)
print("ngram :", result)
