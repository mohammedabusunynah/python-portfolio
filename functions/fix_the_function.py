# fix_the_functions.py
# this program is a login report

# error 1 (runtime): you can't call a function before defining it (moved it down where it should be)



def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
# error 4 (runtime): total never returned so the result was 0 always        
        return failed * minutes
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"

# error 2 (runtime): there was user instead of username
print_header()
print(login_line(username="sara", failed=4))
# error 3 (semantic): a missing print function for the login_line("omar, 1")
print(login_line("omar", 1))