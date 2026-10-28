# login_report.py
# this program prints a login report 

MAX_LOGIN_ATTEMPTS = 5 

username = input("username: ")
failed = int(input("failed attempts: "))
attempts_left = MAX_LOGIN_ATTEMPTS - failed

print("=" * 30)
print("LOGIN REPORT")
<<<<<<< HEAD
print("="*30)

=======
print("=" * 30)
# double \t to make it in the same line in the terminal in vscode (it was not at the same level with only one \t )
>>>>>>> b2d7a776c5159b29d1d69bbbe1ce96bdfad20c1d
print(f"user:\t\t{username}\nfailed:\t{failed}\nattempts left:\t{attempts_left}")

