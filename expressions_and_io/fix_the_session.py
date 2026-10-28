# fix_the_session.py
# This program reports a user's session time.
# 

username = input("Username: ")
# (runtime error) first error: the input always shows the result as a str even if the value is a number so if you want to do a mathmatical operation you need to convert it and that what was missing, the int before the input in total_seconds
total_seconds = int(input("Session length in seconds: "))
# (semantic error): the used division is (/) not (//) that shows a decimal point in minutes
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
# (semantic error): missing f prefix, and missing it can print the {username} not it's value 
print(f"User: {username}")
# (runtime error) second error: the minutes is int and what's behind it and the after it is str and the concatenatenation can't mix str with int 
print("Session: " + str(minutes) + " min " + str(seconds) + " s")
print("=" * 30)
