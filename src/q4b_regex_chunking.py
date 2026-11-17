# 4b: Write a program to extract specific patterns from a given sample sentence
# using regular expression-based chunking.

import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

sentence = input("Enter a sentence: ")
tagged = nltk.pos_tag(word_tokenize(sentence))

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
parser = RegexpParser(grammar)
tree = parser.parse(tagged)

print(tree)
for subtree in tree.subtrees(filter=lambda t: t.label() == "NP"):
  print("NP chunk:", " ".join(word for word, _ in subtree.leaves()))
