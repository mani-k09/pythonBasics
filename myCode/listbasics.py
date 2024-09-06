print("here we practise on List input")
print("##########")

calculation_units = 24
unit = "Hours"


def calulate_days(user_input):
    try:
        if user_input.isdigit():
            total_days = int(user_input)
            if total_days > 0:
                print(f"{total_days} are {total_days * calculation_units} {unit}")
                #print("calculation completed")
            elif total_days == 0:
                print("you have entered a 0, Pleases enter days greater than 0")
        else:
            print(f"Your input ' {user_input} ' is incorrect and not allowed")
    except ValueError:
        print("The value error was handled")

user_input =""
while user_input != "exit":
    user_input = input("enter the number of days in comma separated ,then I will calculate the hours,otherwise type 'exit'\n")
    #print(type(user_input.split(",")))
    #print(user_input.split(","))
    for num_of_days in user_input.split(","):
        calulate_days(num_of_days)
