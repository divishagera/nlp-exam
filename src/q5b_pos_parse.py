# 5b: Write a program to demonstrate how to use the nltk library to process text
# and generate a part-of-speech tag for each word and draw the parsed result.

import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

text = input("Enter a sentence: ")
pos_tags = nltk.pos_tag(word_tokenize(text))

print("POS Tags:", pos_tags)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
tree = RegexpParser(grammar).parse(pos_tags)

print("Parsed Tree:")
print(tree)
# tree.draw()  # Uncomment to open the Tkinter tree window on a desktop display
