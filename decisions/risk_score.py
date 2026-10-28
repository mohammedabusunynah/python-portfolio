# risk_score.py
# a risk score measurement program

score = 0
failed = int(input("failed attempts in the last hour: "))
login_hour = int(input("login hour:"))
device_state = input("new device (yes/no): ")

if failed >= 3:
    score += 40
if login_hour < 6:
    score += 30
if device_state == "yes":
    score += 30

if score >= 70:
    level = "High"
elif score >= 30:
    level = "Medium" 
else:
    level = "Low"
print(f"Risk score: {score} ({level})")