# pin_space_table.py 
# how long it takes to guess every pin according to it's length

GUESSES_PER_SECOND = 10

for digits in range(4, 9):
    combinations = 10 ** digits 
    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = seconds// 86400
    print(f"{digits} digits: {combinations} PINS, {minutes} minutes, {days} days")