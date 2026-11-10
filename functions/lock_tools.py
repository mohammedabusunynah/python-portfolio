# lock_tools.py
# this program is a lock tool that lock after a number of failed attempts

def is_locked(failed, max_tries=3):
    """return True or False depending on the number of failed tries with a limit to the number of tries"""
    if failed >= max_tries:
        return True
    return False


def tries_left(failed, max_tries=3):
    """return a 0 if is_locked == true or it subtract from the max_tries the failed attempts"""
    if is_locked(failed, max_tries):
        return 0
    return max_tries - failed


def status(failed):
    """Returns "locked" or "active" depending on the is_locked state and calculate the left from tries_left"""
    if is_locked(failed):
        return "locked"
    left = tries_left(failed)
    return f"active ({left} tries left)" 
    

print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))