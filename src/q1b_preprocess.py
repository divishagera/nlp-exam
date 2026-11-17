# 1b: Write a program to Perform Preprocessing (Tokenization, Stop Word Removal
# and Stemming) of Text.

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

example_string = input("Enter text to preprocess: ").strip()
if not example_string:
    example_string = "There is a man on the hill, and I watched him. He has a telescope. I am on a hill and I saw a man using my telescope. I am on a hill and I saw a man with a telescope."

sentences = nltk.sent_tokenize(example_string)
print(sentences)

words = nltk.word_tokenize(example_string)
print(words)

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

for i in range(len(sentences)):
    sent_words = nltk.word_tokenize(sentences[i])
    sent_words = [stemmer.stem(word) for word in sent_words if word.lower() not in stop_words]
    sentences[i] = " ".join(sent_words)

print(sent_words)
print(sentences)
