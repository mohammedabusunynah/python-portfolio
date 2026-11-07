# port_report.py
# this program prints the port and it's type

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

count = 0

for port in range(start_port, end_port + 1):
    count += 1
    if 0 <= port <= 1023:
        print(f"{port}: system")
    elif 1024 <= port <= 49151:
        print(f"{port}: user")
    elif 49152 <= port <= 65535:
        print(f"{port}: dynamic")

print(f"Ports checked: {count}")