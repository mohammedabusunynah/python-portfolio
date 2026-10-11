# fix_the_record.py
# this file contain four bugs and i have to debug them.
# This program prints a short record about a network device.

device_name = "edge-router"
# (syntaxerro): invalid decimal literal 
second_ip = "192.0.2.1"
# (syntaxerror): invalid syntax 
type = "router"
# (runtime error) ValueError:invalid literal for int() 
port = str("twenty-two")
# (runtime error) NameError 
print("Device:", device_name)
print("Backup IP:", second_ip)
print("Type:", type) 
print("Port:", port)

# bugs that appears first in order 
# 1:line 5 syntax error:invalid decimal literal (because it starts with the number 2 and it's aginst the naming rules)
# 2:line 6 syntaxerror invalid syntax (because of using class which is a keyword for python)
# 3:line 7 valueError:invalid literal for int() (because it's int and what's inside the () is a text)
# 4:line 8 nameerror (because e is not there in device_name)

# note: i have fix the bugs by replacing the variables or changing the functions