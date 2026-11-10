# password_check.py
# this program checks if the pasword is valid or not

def long_enough(password, minimum=8):
    """If the password length is longer than or equal to the minimum return True."""
    return len(password) >= minimum


def differs_from_username(password, username):
    """Returns True if password is not the same as the username."""
    if password != username:
        return True 
    return False


def password_ok(password, username):
    """Return True if two checks passed correctly."""
    if differs_from_username(password, username) and long_enough(password, minimum=8):
        return True
    return False


username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Passowrd rejected.")










