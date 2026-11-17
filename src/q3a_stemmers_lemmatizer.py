# 3a: Write a program to analyze the different types of Stemmers and Lemmatizer.

import nltk
from nltk.stem import LancasterStemmer, PorterStemmer, SnowballStemmer, WordNetLemmatizer

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

words = input("Enter words separated by space: ").split()

porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()

for w in words:
  w_low = w.lower()
  print(
      f"{w} -> Porter: {porter.stem(w_low)} | "
      f"Snowball: {snowball.stem(w_low)} | "
      f"Lancaster: {lancaster.stem(w_low)} | "
      f"Lemma (noun): {lemmatizer.lemmatize(w_low, pos='n')} | "
      f"Lemma (verb): {lemmatizer.lemmatize(w_low, pos='v')}"
  )
