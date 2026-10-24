# device_card.py
# this is a device record card, printing variables and changing the value of two variables and printing them in one line

MAX_CONNECTIONS = 20
deivce_name = "thinkpad-E16"
device_ip = "192.0.2.12"
service = "HTTP"
open_port = 80

print("Device name:", deivce_name)
print("IP address:", device_ip)
print("Service:", service)
print("Port:", open_port)
print("Max connections:", MAX_CONNECTIONS)
# changing the two values

service = "HTTPS"
open_port = 443

print("service:", service, "on port:", open_port)


