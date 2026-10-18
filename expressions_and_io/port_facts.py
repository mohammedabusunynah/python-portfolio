# port_facts.py
# this program calculates the number of ports, possible ipv4 adresses and highest port number then puts the result in f string

# (RFC 9293) In the TCP header, Source Port and Destination Port are 16 bits each.
# (RFC 791) "Addresses are fixed length of four octets (32 bits)."


PORT_BITS = 16
IPV4_BITS = 32

possible_port_numbers = 2**PORT_BITS 
highest_port_number = 2**16-1
number_of_possible_ipv4 = 2**IPV4_BITS

print(f"number of possible ports: {possible_port_numbers}")
print(f"highest port number: {highest_port_number}")
print(f"possible ipv4 adresses: {number_of_possible_ipv4}")