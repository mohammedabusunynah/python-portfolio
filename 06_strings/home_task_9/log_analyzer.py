# log_analyzer.py

ALERT_LIMIT = 3
LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""

lines = LOG.split("\n")


def get_field(line, name):
    start = line.find(name + "=")
    if start == -1:
        return ""
    start = start + len(name) + 1
    end = line.find(" ", start)
    if end == -1:
        end = len(line)
    return line[start:end]


def get_status(line):
    return line.split()[1]


def count_status(status):
    count = 0
    for line in lines:
        if get_status(line) == status:
            count = count + 1
    return count


def show_summary():
    print("Lines:", len(lines))
    print("Failed:", count_status("FAILED"))
    print("OK:", count_status("OK"))


def search(keyword):
    matches = 0
    n = 1
    for line in lines:
        if keyword.lower() in line.lower():
            print(str(n) + ": " + line)
            matches = matches + 1
        n = n + 1
    print("Matches:", matches)


def ip_report(ip):
    total = 0
    for line in lines:
        if get_status(line) == "FAILED" and get_field(line, "ip") == ip:
            print(line.split()[0], get_field(line, "user"))
            total = total + 1
    print("Failed logins from " + ip + ": " + str(total))
    if total >= ALERT_LIMIT:
        print("ALERT: possible password guessing.")


def mask(word):
    if len(word) <= 2:
        return "*" * len(word)
    return word[0] + "*" * (len(word) - 2) + word[-1]


def show_masked():
    for line in lines:
        user = get_field(line, "user")
        print(line.replace("user=" + user, "user=" + mask(user)))


def show_menu():
    print("AUTH LOG ANALYZER")
    print("1. Summary")
    print("2. Search")
    print("3. IP report")
    print("4. Masked log")
    print("q. Quit")


show_menu()
while True:
    choice = input("Choice: ").strip().lower()
    if choice == "1":
        show_summary()
    elif choice == "2":
        keyword = input("Keyword: ").strip()
        search(keyword)
    elif choice == "3":
        ip = input("IP: ").strip()
        ip_report(ip)
    elif choice == "4":
        show_masked()
    elif choice == "q":
        print("Bye.")
        break
    else:
        print("Unknown choice.")