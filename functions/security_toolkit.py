# security_toolkit.py
# this program is a security toolkit that has multiple functios and tools used to check certien things

MIN_LENGTH = 8

def border(width):
    """Prints a border design"""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
        """Prints a border for the text"""
        border(len(text))
        print("| " + text + " |")
        border(len(text))

def show_menu():
      """Prints a title and 4 menu lines"""
      print("SECURITY TOOLKIT")     
      print("1. Check a port")
      print("2. Check a password")
      print("3. PIN guessing time")
      print("q. Quit")   


def port_range(port):   
      """Checks if the port is valid or not"""
      if port < 0 or port > 65535:
            return "invalid"
      elif port <= 1023:
            return "system"
      elif port <= 49151:
            return "user"
      return "dynamic"


def check_port():
    """Ask the user for the port number and call the show_box()"""
    port = int(input("Port: "))
    show_box("Port " + str(port) + ": " + port_range(port))



def password_problem(password, username):
    """A condition for the password"""
    if len(password) < MIN_LENGTH:
        return "too short"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Ask the user for username and password and checks if there is any problems with the password."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem:
        show_box("Rejected: " + problem)
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Counts how much days it takes to crack the PIN."""
    return 10 ** digits // per_second // 86400


def check_pin():
    """Ask for digits & guesses per second then call the days_to_guess(digits, per_second) then shows it the show_box"""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(str(digits) + " digits: " + str(days) + " days")


show_menu()
checks = 0
while True:
    choice = input("Choice (1, 2, 3, or q): ")
    if choice == "1":
        check_port()
        checks += 1
    elif choice == "2":
        check_password()
        checks += 1
    elif choice == "3":
        check_pin()
        checks += 1
    elif choice == "q":
        break
    else:
        print("Unknown choice.")
show_box("Checks done: " + str(checks))
