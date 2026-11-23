num1 =int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
choice = input("Enter any operator to perform operation :")
if choice == "+" :
    sum = num1 + num2 
    print("Addition of num1 and num2 is :",sum)
if choice == "-" :
    subtract = num1 - num2 
    print("Subtraction of num1 and num2 is :",subtract)
if choice == "*" :
    multiplication = num1 * num2 
    print("Multiplication of num1 and num2 is :",multiplication)
if choice == "/" :
    divide = num1 / num2 
    print("division of num1 and num2 is :",divide)
if choice == "%" :
    modulus = num1 % num2 
    print("modulus of num1 and num2 is :",modulus)
if choice == "//" :
    floordiv = num1 // num2 
    print("Floordiv of num1 and num2 is :",floordiv)
if choice == "**" :
    exponent = num1 ** num2 
    print("Exponent of num1 and num2 is :",exponent)
    