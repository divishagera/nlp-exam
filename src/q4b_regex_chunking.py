# 4b: Write a program to extract specific patterns from a given sample sentence
# using regular expression-based chunking.

import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

PatternToFind = r"""
NP: {<DT>?<JJ>*<NN>}
NP: {<NNP>+}
"""

Sentence = input("Enter a sentence: ").strip()
if not Sentence:
    Sentence = "This is a very good book. I felt really nice reading it."

SentenceWord = nltk.word_tokenize(Sentence)
SentencePos = nltk.pos_tag(SentenceWord)

PatternParser = nltk.RegexpParser(PatternToFind)
ParsedResults = PatternParser.parse(SentencePos)

for results in ParsedResults:
    if type(results) == nltk.tree.Tree:
        print(results)
