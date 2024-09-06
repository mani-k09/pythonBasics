#from support import helpers
from steps.helpers import calulate_days

print("Lets explore how python dictionary works")
print("It helps to store data in key value pair format")
print("###########")

"""theDict={"name":"ManU","location":"manchester","game":"footBall","rank":5,"players":11}
print(f"The dictionary has : {theDict}")
print(theDict["name"])
print(len(theDict))"""


"""def calculate_value(num_of_days,calc_units):
    if calc_units == "hours":
        return (f"{num_of_days} are {num_of_days * 24} {calc_units}")
    elif calc_units == "minutes":
        return (f"{num_of_days} are {num_of_days * 24 * 60} {calc_units}")
    else:
        return "Unsupported unit" """

"""def calulate_days(days_and_unit_dict):
    try:
        if days_and_unit_dict['days'].isdigit():
            total_days = int(days_and_unit_dict['days'])
            print(total_days)
            print(days_and_unit_dict['unit'])
            if total_days > 0:
                the_Calculated_value= helpers.calculate_value(total_days,days_and_unit_dict['unit'])
                print(the_Calculated_value)
                print("calculation completed")
            elif total_days == 0:
                print("you have entered a 0, Pleases enter days greater than 0")
        else:
            print(f"Your input ' {days_and_unit_dict['days']} ' is incorrect and not allowed")
    except ValueError:
        print("The value error was handled") """

user_input =""
while user_input != "exit":
    user_input = input("Enter the days and unit in the days:unit format\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict ={"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dict)
    calulate_days(days_and_unit_dict)
