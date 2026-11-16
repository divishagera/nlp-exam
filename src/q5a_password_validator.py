# 5a: Write a Python program to validate a password based on the following
# security requirements. The program should accept a password from the user and
# check whether it satisfies all the given criteria: The password must contain
# at least 8 characters. It must contain at least one uppercase letter (A-Z). It
# must contain at least one lowercase letter (a-z). It must contain at least one
# digit (0-9). It must contain at least one special character (e.g., @, #, $, %,
# &, ).

import re


def validate_password(password):
  errors = []
  if len(password) < 8:
    errors.append("must contain at least 8 characters")
  if not re.search(r"[A-Z]", password):
    errors.append("must contain at least one uppercase letter (A-Z)")
  if not re.search(r"[a-z]", password):
    errors.append("must contain at least one lowercase letter (a-z)")
  if not re.search(r"\d", password):
    errors.append("must contain at least one digit (0-9)")
  if not re.search(r"[@#$%&*!^()_+\-=\[\]{};':\"\|,.<>/?]", password):
    errors.append("must contain at least one special character")

  if not errors:
    return True, "Valid password: satisfies all security requirements."
  return False, "Invalid password: " + "; ".join(errors) + "."


if __name__ == "__main__":
  password = input("Enter a password to validate: ")
  is_valid, message = validate_password(password)
  print(message)
