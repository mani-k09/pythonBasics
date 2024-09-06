print("here we practise on nested IF")
print("##########")

calculation_units = 24
unit = "Hours"


def calulate_days(user_input):
    try:
        if user_input.isdigit():
            total_days = int(user_input)
            if total_days > 0:
                print(f"{total_days} are {total_days * calculation_units} {unit}")
                print("calculation completed")
            elif total_days == 0:
                print("you have entered a 0, Pls enter days greater than 0")
        else:
            total_days = int(user_input)
            print('Your input is incorrect and not allowed')
    except ValueError:
        print("The value error was handled")

user_input =""
while user_input != "exit":
    user_input = input("enter the number of days \n")
    calulate_days(user_input)
