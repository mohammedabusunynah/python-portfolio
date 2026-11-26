# fix_the_parser.py
LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
# semantic error: should be line[0:5] not line[0:4]
    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
# semantic error: you if you used .lower() but didn't save it in a variable it will be gone and nothing will show in the result
    user = user.lower()
    return user


def is_failed(line):
    """Return True if the line reports a failed login."""
# semantic error: it returns false instead of true there should be .lower() after line
    return "failed" in line.lower()


def hide_first(user):
    """Return user with its first letter replaced by *."""
# runtime error: you can't change the values like this (user[0] = "*") or it will give an error 
    return  "*" + user[1:]
    


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
# runtime error: won't work because .len() is not a method 
print(f"Length: {len(LINE)}")