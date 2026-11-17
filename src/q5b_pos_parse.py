# 5b: Write a program to demonstrate how to use the nltk library to process text
# and generate a part-of-speech tag for each word and draw the parsed result.

import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

sentence = input("Enter a sentence for POS tagging and parsing: ").strip()
if not sentence:
    sentence = "The clever student solved the hard problem."

pos_tags = nltk.pos_tag(word_tokenize(sentence))
print("POS Tags:", pos_tags)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
tree = RegexpParser(grammar).parse(pos_tags)
print("Parsed Tree:")
print(tree)
# tree.draw()  # Uncomment to open graphical tree window on desktop
