# fix_the_policy.py
# Check a new password against an example policy and classify its length.

MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# missing colon in the end (#1)
if len(password) < MIN_LENGTH:
    print("- Too short.")
# should be if not elif, because it only chose one of them in this case the first one, but in what we need is is the two conditions to be checked (#2)
if password == username:
    print("- Same as the username.")

# in the first if should be 16 not MIN_LENGTH and the valuse inside the strength will differ
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"
# this was part of else which it should not be (#3)
print(f"Length: {len(password)} ({strength})")