# 5b: Write a program to demonstrate how to use the nltk library to process text
# and generate a part-of-speech tag for each word and draw the parsed result.

import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

for pkg in [
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger",
    "averaged_perceptron_tagger_eng",
]:
  nltk.download(pkg, quiet=True)


def pos_and_parse(sentence, draw_gui=False):
  tokens = word_tokenize(sentence)
  pos_tags = nltk.pos_tag(tokens)

  grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    PP: {<IN><NP>}
    VP: {<VB.*><NP|PP>*}
  """
  parser = RegexpParser(grammar)
  parsed_tree = parser.parse(pos_tags)

  print("\nWord -> POS Tag:")
  for word, tag in pos_tags:
    print(f"  {word:<12} : {tag}")

  print("\nParsed Tree:")
  print(parsed_tree)

  if draw_gui:
    # Opens Tkinter canvas window when running locally with a display
    parsed_tree.draw()


if __name__ == "__main__":
  default_text = "The young engineer built a smart voice assistant."
  user_text = input(
      "Enter a sentence to tag and parse (or press Enter for default): "
  ).strip()
  text = user_text if user_text else default_text

  pos_and_parse(text, draw_gui=False)
