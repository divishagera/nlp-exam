# 1a: Write a program to extract email, data, phone number from text files using
# Python regular expression? (Note: "data" in the syllabus sheet corresponds to
# date extraction.)

import re


def extract_data(file_path):
  with open(file_path, "r") as f:
    text = f.read()

  emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
  phones = re.findall(r"\b\d{10}\b", text)
  dates = re.findall(r"\b\d{2,3}-\d{2,3}-\d{4}\b", text)

  print(emails)
  print(phones)
  print(dates)


extract_data("demo.txt")
