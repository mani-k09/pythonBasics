import os
import logging
import json
import datetime

print(f"the os name {os.name}")
"""logger =logging.getLogger("MAIN")
logger.info("Test Info")
logger.error("Test Error")
logger.warning("Test Warning")"""


userData = input("enter the goal and the date like to accomplish in the followig format Goal:dd.mm.yyyy\n")
user_input=userData.split(":")
goal = user_input[0]
days = user_input[1]
#print(goal)
#print(days)
target_date = datetime.datetime.strptime(days,'%d.%m.%Y')
today=datetime.datetime.today()
time_till= target_date -today
print(f"Hey user, time remaining for the goal {goal} is {time_till.days} days")
#print(target_date)
#print(type(target_date))

#print(datetime.datetime.today())

#print(time_till)