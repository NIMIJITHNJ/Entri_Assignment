num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

op = int(input("Enter the function to be performed (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for modulus, 6 for exponential):"))

if op == 1:
    print("Value of addition:",num1+num2)
elif op == 2:
    print("Value of subtraction:",num1-num2)
elif op == 3:
    print("Value of multiplication:",num1*num2)
elif op == 4:
    print("Value of division(float):",num1/num2)
    print("Value of division(integer):",num1//num2)
elif op == 5:
    print("Value of modulus:",num1%num2)
else:
    print("Value of exponential:",num1**num2)