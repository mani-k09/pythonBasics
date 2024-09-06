print("Here we'll practise on conditional statements")
print("######")

calculation_units=24
unit= "Hours"

def calulate_days(days_entered):
    if days_entered > 0:
        print(f"{days_entered} are {days_entered * calculation_units} {unit}")
        print("calculation completed")
        #return "calculation completed return"
    elif days_entered == 0:
        #return "you have entered a 0, Pls enter days greater than 0"
        print("you have entered a 0, Pls enter days greater than 0")
    else:
       #return "Incorrect value entered"
       print('Incorrect value entered')

user_input = input("enter the number of days \n")
if user_input.isdigit():
    total_days = int(user_input)
    calulate_days(total_days)
else:
    print("Your inout is incorrect and not allowed")


