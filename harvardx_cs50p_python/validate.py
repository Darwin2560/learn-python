import re

email = input("What's your email address? ").strip()

# re.search(pattern, string, flags)
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
