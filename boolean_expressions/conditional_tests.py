# conditional_tests.py
# this program to predict then run conditions and comparisons 

user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is failed >= 3? i predict True.")
print(failed >= 3)

print("\nIs user == 'admin'? i predict False.")
print(user == "admin")

print("\nIs port != 80? i predict True.")
print(port != 80)

# mistake? because i put 3 after the comparing mark (i fixed it later) print("\nIs failed > 3? i predict true")
print("\nIs failed > 2? i predict true ")
print(failed > 2)

print("\nIs port < 30? i predict true")
print(port < 30 )

print("\nIs port <= 22? i predict true")
print(port <= 22)

# did not match the prediction? i was expecting it to be false but was true because i didn't make any of the valuse false and i used and (i fixed it later) print("\nIs role == viewer and user == analyst? i predict false")
print("\nIs role == 'viewer' and user == 'admin'? i predict false")
print(role == "viewer" and user == "admin")

print("\nIs failed == 4 or port != 22? i predict false")
print(failed == 4 or port != 22)

print("\nIs user == 'analyst' and not failed == 3? i predict false")
print(user == "analyst" and not failed == 3)

print("\nIs failed != 3 or not port != 33? i predict false")
print(failed != 3 or not port != 33)

