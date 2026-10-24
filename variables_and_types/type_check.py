# type_check.py
# this program is for checking the type of the value & convert and print the converted value with its type in one print

print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))
# this print for an empty line to make it look decent in the terminal
print()
# prediction: 1:int 2:str 3:float 4:str 5:int

int("443")
str(8080)
float(2.5)

print(int("443"), type(int("443")))
print(str(8080), type(str(8080)))
print(float(2.5), type(float(2.5)))
