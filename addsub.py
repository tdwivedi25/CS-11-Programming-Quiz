opp = input("Do you want to do addition or subtraction? ")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

def addition():
    return a + b

def subtraction():
    return a - b

if opp == "addition":
    print(addition())

if opp == "subtraction":
    print(subtraction())