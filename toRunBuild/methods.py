print("Here we practise about functions/methods")
print('============')

calculationUnits = 60
nameOfUnit ="seconds"

def calculate_units():
    print(f"10 days are {10 * calculationUnits } { nameOfUnit }")
    print("The method being called")

def calculate_units_runtime(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculationUnits} {nameOfUnit}")
    print("The method being called wiht parameter")

def calculate_unit_with_message(num_of_days,customeMessage):
    print(f"{num_of_days} days are {num_of_days * calculationUnits} {nameOfUnit}")
    print(customeMessage)

def scope_check(local_varibale):
    my_var ="inside function varibale"
    print(f"global varibale : {calculationUnits}")
    print(f"localVaribale:  { local_varibale}")
    print("inside function :" + my_var)

def testPrint():
    print(f"print the multiplication of {10 * 5}")

testPrint()
calculate_units()
calculate_units_runtime(10)
calculate_unit_with_message(10,"This is Great !")
scope_check(25)