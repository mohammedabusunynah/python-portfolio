# session_timer.py
# this program creats a session timer 

session_length = int(input("enter session lenght in seconds"))
minutes = session_length // 60
seconds = session_length % 60
print(f"session length in seconds: {session_length} \nsession length: {minutes} minute and {seconds} seconds")

# testing numbers: 905 --> 15 min & 5 sec
# testing numbers: 60 --> 1 minute & 0 sec
# testing numbers: 59 --> 0 minutes & 59 sec
