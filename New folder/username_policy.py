# username_policy.py

MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Cleans the username."""
    return username.strip().lower()


def bad_character(username):
    """"Returns the character that's not letter or digit or _, or returns ""."""
    for letter in username:
        if not letter.isalpha() and not letter.isdigit() and letter != "_":
            return letter

    return ""


def policy_problem(username):
    """Returns the policy problems."""
    if len(username) < MIN_LENGTH or len(username) > MAX_LENGTH:
        return "length must be 3 to 12."
    if not username[0].isalpha():
        return "it must start with a letter."
    character = bad_character(username)
    if character != "":
        return "the character " + character + " is not allowed."
    return ""


username = input("New username: ")
username_cleaned = clean(username)
problem = policy_problem(username)

if problem == "":
    print("Accepted [" + username + "].")
else:
    print("Rejected [" + username + "]: " + problem)