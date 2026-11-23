num = int(input("Enter a three digit number :")) 
if 100 <= num <= 999 :
    d1 = (num // 100 ) 
    d2 = (num // 10) % 10 
    d3 = (num % 10) 
    if ((d1 ** 3) + (d2 ** 3 )+ ( d3 ** 3) == num ):
        print("Number is an armstrong number !")
    else :
        print("Number is not an armstrong number !") 
else :
    print("invalid input !")