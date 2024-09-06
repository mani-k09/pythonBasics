print("Here we practise user Input")
print("===========")

calculation_units = 24

def calculate_Hours(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_units} hours")
    print("It was great!")
#Get User Input
Total_days=input("enter the number of days :\n")
#covert user input string to integer
user_entered_dates = int(Total_days)

calculate_Hours(user_entered_dates)
