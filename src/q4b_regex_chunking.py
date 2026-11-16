# 4b: Write a program to extract specific patterns from a given sample sentence
# using regular expression-based chunking.

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


def extract_regex_chunks(sentence):
  tokens = word_tokenize(sentence)
  tagged = nltk.pos_tag(tokens)

  # Chunk grammar for Noun Phrases (NP) and Verb + Noun Phrase patterns
  grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP_NP: {<VB.*><DT>?<JJ.*>*<NN.*>+}
  """
  parser = RegexpParser(grammar)
  tree = parser.parse(tagged)
  return tagged, tree


if __name__ == "__main__":
  default_sentence = (
      "The curious student solved the difficult NLP problem quickly."
  )
  user_sentence = input(
      "Enter a sentence (or press Enter for default sample): "
  ).strip()
  sentence = user_sentence if user_sentence else default_sentence

  tagged, tree = extract_regex_chunks(sentence)
  print("POS Tags:", tagged)
  print("\nChunk Tree:")
  print(tree)

  print("\nExtracted Noun Phrases (NP):")
  for subtree in tree.subtrees(filter=lambda t: t.label() == "NP"):
    print(" -", " ".join(word for word, _ in subtree.leaves()))
