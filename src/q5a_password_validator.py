# 5a: Write a Python program to validate a password based on the following
# security requirements. The program should accept a password from the user and
# check whether it satisfies all the given criteria: The password must contain
# at least 8 characters. It must contain at least one uppercase letter (A-Z). It
# must contain at least one lowercase letter (a-z). It must contain at least one
# digit (0-9). It must contain at least one special character (e.g., @, #, $, %,
# &, ).

import re

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 char long"
    if re.search(r"\s", password):
        return False, "Password mustn't contain spaces"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase"
    if not re.search(r"\d", password):
        return False, "Password must contain at least one no."
    if not re.search(r"[@#$%&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    return True, "Password is valid and secure"

if __name__ == "__main__":
    user_pwd = input("Enter a password (or press Enter to run sample passwords): ").strip()
    if user_pwd:
        valid, message = validate_password(user_pwd)
        print(f"{user_pwd} : {message}")
    else:
        test_passwords = ["weak!", "Password1!", "StrongPass123@"]
        for password in test_passwords:
            valid, message = validate_password(password)
            print(f"{password} : {message}")
