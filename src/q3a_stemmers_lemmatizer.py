# 3a: Write a program to analyze the different types of Stemmers and Lemmatizer.

import nltk
from nltk.stem import LancasterStemmer, PorterStemmer, SnowballStemmer, WordNetLemmatizer

for pkg in ["wordnet", "omw-1.4"]:
  nltk.download(pkg, quiet=True)


def analyze_stemmers_and_lemmatizer(words):
  porter = PorterStemmer()
  lancaster = LancasterStemmer()
  snowball = SnowballStemmer("english")
  lemmatizer = WordNetLemmatizer()

  print(
      f"{'Word':<14} {'Porter':<14} {'Lancaster':<14} {'Snowball':<14}"
      f" {'Lemma (Noun)':<14} {'Lemma (Verb)':<14}"
  )
  print("-" * 86)

  for word in words:
    w = word.lower()
    p_stem = porter.stem(w)
    l_stem = lancaster.stem(w)
    s_stem = snowball.stem(w)
    n_lemma = lemmatizer.lemmatize(w, pos="n")
    v_lemma = lemmatizer.lemmatize(w, pos="v")

    print(
        f"{word:<14} {p_stem:<14} {l_stem:<14} {s_stem:<14}"
        f" {n_lemma:<14} {v_lemma:<14}"
    )


if __name__ == "__main__":
  user_input = input(
      "Enter words separated by spaces (or press Enter for default list): "
  ).strip()
  if user_input:
    word_list = user_input.split()
  else:
    word_list = [
        "running",
        "runs",
        "easily",
        "fairly",
        "studies",
        "studying",
        "better",
        "leaves",
        "cacti",
    ]

  analyze_stemmers_and_lemmatizer(word_list)
