# login_decision.py
# a login decision program

MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("username: ")
failed = int(input("failed attempts so far: "))
password = input("password: ")

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password == STORED_PASSWORD:
    print("Access granted.")
else:
    print("Access denied. Attempts left:", MAX_FAILED - failed - 1)
