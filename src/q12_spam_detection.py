# 12: Write a program to conduct the case study on SMS Spam Detection Analysis
# using Natural language processing. Use an spam.csv data set

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

csv_path = input("Enter spam CSV path (default 'spam.csv'): ").strip() or "spam.csv"
df = pd.read_csv(csv_path, encoding="latin-1")

if {"v1", "v2"}.issubset(df.columns):
    df = df[["v1", "v2"]].rename(columns={"v1": "label", "v2": "message"})
else:
    df = df.iloc[:, :2]
    df.columns = ["label", "message"]

df = df.dropna(subset=["label", "message"])
df["label_num"] = df["label"].str.strip().str.lower().map({"ham": 0, "spam": 1})
df = df.dropna(subset=["label_num"])

X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label_num"], test_size=0.2, random_state=42, stratify=df["label_num"]
)

vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

preds = model.predict(X_test_vec)
print(f"Accuracy: {accuracy_score(y_test, preds):.4f}")
print(classification_report(y_test, preds, target_names=["ham", "spam"]))

custom_msg = input("Enter an SMS message to classify: ").strip()
if custom_msg:
    pred = model.predict(vectorizer.transform([custom_msg]))[0]
    print("Prediction:", "SPAM" if pred == 1 else "HAM")
