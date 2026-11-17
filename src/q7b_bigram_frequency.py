# 7b: Bigram Frequency Across 3 Documents

from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)
nltk.download("stopwords", quiet=True)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

use_custom = input("Enter custom 3 documents? (y/n): ").strip().lower()
if use_custom == "y":
    doc1 = input("Enter Document 1: ")
    doc2 = input("Enter Document 2: ")
    doc3 = input("Enter Document 3: ")
else:
    doc1 = "convolutional neural networks (CNNs) are a class of deep neural networks that have proven to be highly effective"
    doc2 = "Recurrent neural networks (RNNs) are a class of artificial neural networks that are designed to recognize time."
    doc3 = "generative adversarial networks (GANs) are a class of machine learning framework where two neural networks communicate."

docs = [doc1, doc2, doc3]
combined_text = " ".join(docs).lower()
tokens = word_tokenize(combined_text)
tokens = [lemmatizer.lemmatize(t) for t in tokens if t.isalpha() and t not in stop_words]

bi_list = list(bigrams(tokens))
counter = Counter(bi_list)
total_bigrams = len(bi_list)

print(f"Total number of bigrams: {total_bigrams}")
print("Top 5 most common bigrams:")
for bg, freq in counter.most_common(5):
    print(f"{bg} : {freq}")
