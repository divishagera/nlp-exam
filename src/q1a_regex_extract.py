# 1a: Write a program to extract email, data, phone number from text files using
# Python regular expression? (Note: "data" in the syllabus sheet corresponds to
# date extraction.)

import re


def extract_from_file(file_path):
  with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

  emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
  dates = re.findall(
      r"\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2})\b", text
  )
  phones = re.findall(r"\b(?:\+?\d{1,3}[-.\s]?)?\d{10}\b", text)

  return emails, dates, phones


if __name__ == "__main__":
  sample_path = "sample_data.txt"
  with open(sample_path, "w", encoding="utf-8") as f:
    f.write(
        "Reach out to team@example.org or hr@company.com on 16-11-2026 or call"
        " 9876543210."
    )

  emails, dates, phones = extract_from_file(sample_path)
  print("Emails:", emails)
  print("Dates:", dates)
  print("Phone Numbers:", phones)
