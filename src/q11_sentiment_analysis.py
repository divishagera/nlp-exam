# 11: Write a program to conduct the case study on sentiment analysis using
# Natural language processing. Use a vaccination_tweets .csv data set

import re
import warnings
import nltk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
from wordcloud import WordCloud

warnings.filterwarnings("ignore")
style.use("ggplot")

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)

stop_words = set(stopwords.words("english"))
csv_file = input("Enter CSV filename (default 'vaccination_tweets.csv'): ").strip() or "vaccination_tweets.csv"

df = pd.read_csv(csv_file, engine="python", on_bad_lines="warn")
print("\nDataset Preview:")
print(df.head())

text_col = "Text" if "Text" in df.columns else ("text" if "text" in df.columns else df.columns[0])
text_df = df[[text_col]].copy()
text_df.rename(columns={text_col: "text"}, inplace=True)
text_df.dropna(subset=["text"], inplace=True)

stemmer = PorterStemmer()

def data_processing(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text_tokens = word_tokenize(text)
    filtered_text = [word for word in text_tokens if word not in stop_words]
    return " ".join(filtered_text)

def stemming(data):
    words = data.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return " ".join(stemmed_words)

text_df["text"] = text_df["text"].apply(data_processing)
text_df = text_df.drop_duplicates(subset=["text"], keep="first")
text_df["text"] = text_df["text"].apply(stemming)

text_df["polarity"] = text_df["text"].apply(lambda t: TextBlob(t).sentiment.polarity)
text_df["sentiment"] = text_df["polarity"].apply(
    lambda label: "positive" if label > 0 else ("negative" if label < 0 else "neutral")
)

print(text_df[["text", "polarity", "sentiment"]].head())

plt.figure(figsize=(8, 5))
sns.countplot(data=text_df, x="sentiment", hue="sentiment", palette="viridis")
plt.tight_layout()
plt.show()

all_words = " ".join(text_df["text"].dropna().astype(str))
if len(all_words.strip()) > 0:
    fig, ax = plt.subplots(figsize=(10, 5))
    wordcloud = WordCloud(width=1200, height=600).generate(all_words)
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    ax.set_title("Most frequently used words", fontsize=18)
    plt.tight_layout()
    plt.show()
