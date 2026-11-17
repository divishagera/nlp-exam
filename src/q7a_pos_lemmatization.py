# 7a: Write a program to demonstrate Morphological Analysis and Perform
# Lemmatization based on the Parts of Speech on the given text.

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

def morphological_analysis(text):
    words = word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []

    for word, tag in pos_tags:
        pos_category = tag[0].lower()
        pos_category = pos_category if pos_category in ["a", "r", "n", "v"] else None
        if pos_category:
            lemma = lemmatizer.lemmatize(word, pos=pos_category)
        else:
            lemma = lemmatizer.lemmatize(word)
        lemmatized_words.append(lemma)

    return lemmatized_words

sentence = input("Enter a sentence: ").strip()
if not sentence:
    sentence = "I saw a bird and geese fly in the sky. The child was playing with their toys. The bat was hanging by the pot"

morphological_analysis_ans = morphological_analysis(sentence)
print(morphological_analysis_ans)
