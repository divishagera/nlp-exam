# 3a: Write a program to analyze the different types of Stemmers and Lemmatizer.

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

def morphological_analysis(text):
    words = word_tokenize(text)

    porter_stemmer = PorterStemmer()
    porter_stem = [porter_stemmer.stem(word) for word in words]

    lancaster_stemmer = LancasterStemmer()
    lancaster_stem = [lancaster_stemmer.stem(word) for word in words]

    snowball_stemmer = SnowballStemmer("english")
    snowball_stem = [snowball_stemmer.stem(word) for word in words]

    lemmatizer = WordNetLemmatizer()
    lemma = [lemmatizer.lemmatize(word) for word in words]

    print("Original Sentence :", text)
    print("Porter Stemmer :", porter_stem)
    print("Lancaster Stemmer :", lancaster_stem)
    print("Snowball Stemmer :", snowball_stem)
    print("WordNet Lemmatizer :", lemma)

user_sentence = input("Enter a sentence: ").strip()
if not user_sentence:
    user_sentence = "The striped bats are hanging on their feet for best"

morphological_analysis(user_sentence)
