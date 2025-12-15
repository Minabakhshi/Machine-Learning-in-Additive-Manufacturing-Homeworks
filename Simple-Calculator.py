#Q1- Simple Calculator

numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+  -  *  /): ")

if operator == "+":
    print(numb1 + numb2)

elif operator == "-":
    print(numb1 - numb2)

elif operator == "*":
    print(numb1 * numb2)

elif operator == "/":
    if numb2 == 0:
        print("Error: division by zero is not allowed!")
    else:
        print(numb1 / numb2)

else:

    print("Invalid operator! Use only +  -  *  /")

