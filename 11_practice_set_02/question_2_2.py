num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter an operation (+, -, *, /): ")

match op:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)
    case _:
        print("Enter a valid operation!")
