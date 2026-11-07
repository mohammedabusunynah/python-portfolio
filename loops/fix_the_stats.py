# fix_the_stats.py (fixed)
# Count failed logins and the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# semantic error: the failed counter has to start at 0 before the loop (outsied the loop). (error number 1)
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1
# semantic error: you should use the ( / ) division not the ( // ) because the last gives no decimal point when the requierd answer comes with a decimal point. (error number 2)
# semantic error: this part should not be indented because it would print it multiple times when it should print it once. (error number 3)
print(f"Average session: {total / count} minutes")

# semantic error: it should be range(1, 5) not range(2, 4) because the last number in range is not included. (error number 4)
for level in range(1, 5):
    print(f"Level {level}")