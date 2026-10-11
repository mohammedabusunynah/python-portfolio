# int_research.py

# 1: int(" 22 ") will word because int() ignores the space before and after teh number aand the resul is 22
# 2: int("+22") will work because a leading (-) (+) sings are allowed according to the website and the result is 22
# 3: int("0022") will work because the int() doesn't write leading zeros and the result is 22
# 4: int("2_2") will work because the underscore is allowed between digits in python and teh result is 22

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))

#https://docs.python.org/3/builtins/functions.html#int
