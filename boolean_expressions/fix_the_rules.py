# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")

# input gives a str so we need to convert it to int (second error appeared)
port = int(input("Port: ")) 

# missin = after role (there was only one '=') (third to fix)
is_admin = role == "admin"

# the (<) should be on the left of (=) not the right (first error appeared)
is_system_port = port <= 1023

# there was a missin (port == 443) if there was no comparison on the left and there was a valuse and the first was false then the right valuse will be chosed (fourth to to fix)
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")

print(f"System port: {is_system_port}")

print(f"Web port: {is_web_port}")