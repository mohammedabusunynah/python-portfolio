# access_check.py
# this program is to check access 

MAX_FAILED = 5

role = input("enter role: ")
mfa = input("MFA passed (yes/no): ")
failed = int(input("failed attempts: "))

mfa_ok = mfa == "yes"
is_privileged = role == "admin" or role == "root"
can_log_in = mfa_ok and failed < MAX_FAILED

print(f"MFA OK: {mfa_ok}")
print(f"Privileged role: {is_privileged}")
print(f"Can log in: {can_log_in}")

# note i used some help to explain what's needed from the slide from ai then i wrote the code on a text editor then paste it in vscode to compare the result with what i wrote and the result is decent!!
