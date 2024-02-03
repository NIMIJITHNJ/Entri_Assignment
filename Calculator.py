import AR_Oper_Module

num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))

op = int(input("Enter the function to be performed (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for modulus, 6 for exponential):"))

if op == 1:
    print("Value of addition:",AR_Oper_Module.addition(num1,num2))
elif op == 2:
    print("Value of subtraction:",AR_Oper_Module.subtract(num1,num2))
elif op == 3:
    print("Value of multiplication:",AR_Oper_Module.multiply(num1,num2))
elif op == 4:
    print("Value of division(float):",AR_Oper_Module.divide(num1,num2))
    print("Value of division(integer):",AR_Oper_Module.divide1(num1,num2))
elif op == 5:
    print("Value of modulus:",AR_Oper_Module.modulus(num1,num2))
else:
    print("Value of exponential:",AR_Oper_Module.exponent(num1,num2))