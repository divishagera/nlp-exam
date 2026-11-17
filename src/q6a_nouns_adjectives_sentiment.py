# 6a: Write a program identify nouns and adjectives from the given sentence and
# calculates the overall sentiment score of the extracted adjectives using
# Chunking in natural language processing (NLP)

import nltk
from textblob import TextBlob

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

sentence = input("Enter a sentence: ").strip()
if not sentence:
    sentence = "Ram is a bad leader. He misguides the team"

sentence_word = nltk.word_tokenize(sentence)
sentence_pos = nltk.pos_tag(sentence_word)

onlynouns = " ".join([word for word, postag in sentence_pos if postag in ["NN", "NNP"]])
onlyadjectives = " ".join([word for word, postag in sentence_pos if postag in ["JJ", "JJR", "JJS"]])

print("Noun :", onlynouns)
print("Adjectives:", onlyadjectives)
print("Overall sentiment score of adjectives :", TextBlob(onlyadjectives).sentiment)
