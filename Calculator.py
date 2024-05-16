from ast import operator


operator = input("Enter an operator (+ - * /): ")

firstNum = float(input("Enter the first number : "))
secondNum = float(input("Enter the second number : "))

if operator == "+":
    result = firstNum + secondNum
    print(result)
elif operator == "-":
    result = firstNum - secondNum
    print(result)
elif operator == "*":
    result = firstNum * secondNum
    print(result)
elif operator == "/":
    result = firstNum / secondNum
    print(result)
else:
    print("Invalid Operator")