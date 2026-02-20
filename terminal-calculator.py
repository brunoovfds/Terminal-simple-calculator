# Simple terminal calculator 1st project
# number operators available (+ - * /)
# 1st we need to ask which operator the user is going to use
# 2nd the 1st and 2nd number to make the operation
# 3rd return the final answer
# 4th print error



def calculate(operator, number, number2):
    #operator = input("Choose your first operator: + - * /")
    if operator == "+":
        print(int(number + number2))
    elif operator == "-":
        print(int(number - number2))
    elif operator == "*":
        print(int(number * number2))
    elif operator == "/":
        print(int(number / number2))
    else:
        print("Invalid Operator \n Operators Available \n + - * /")
calculate(operator = input(" + - * / \n"), number = float(input("Choose your first number: ")), number2 = float(input("Choose your second number: ")))