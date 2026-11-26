# ip_checker.py

def is_valid_part(part):
    """"Checks if the the part of the ip is valid."""
    return part.isdecimal() and int(part) <= 255




def ip_problem(address):
    """Checks for ip problems and returns them."""
    if address.count(".") != 3:
        return "Invalid: it needs exactly 3 dots."
    parts = address.split(".")
    for part in parts:
        if part == "":
            return "Invalid: a part is empty."
        if not is_valid_part(part):
            return part + " is not a number from 0 to 255"
    return ""
        

address = input("IPv4 address: ").strip()
problem = ip_problem(address)
if problem == "":
    print(address, "is valid.")
else:
    print("Invalid:", problem)






















    