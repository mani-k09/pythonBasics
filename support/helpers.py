


"""def calculate_value(num_of_days,calc_units):
    if calc_units == "hours":
        return (f"{num_of_days} days are {num_of_days * 24} {calc_units}")
    elif calc_units == "minutes":
        return (f"{num_of_days} days are {num_of_days * 24 * 60} {calc_units}")
    else:
        return "Unsupported unit"

def calulate_days(days_and_unit_dict):
    try:
        if days_and_unit_dict['days'].isdigit():
            total_days = int(days_and_unit_dict['days'])
            print(total_days)
            print(days_and_unit_dict['unit'])
            if total_days > 0:
                the_Calculated_value= calculate_value(total_days,days_and_unit_dict['unit'])
                print(the_Calculated_value)
                print("calculation completed")
            elif total_days == 0:
                print("you have entered a 0, Pleases enter days greater than 0")
        else:
            print(f"Your input ' {days_and_unit_dict['days']} ' is incorrect and not allowed")
    except ValueError:
        print("The value error was handled") """