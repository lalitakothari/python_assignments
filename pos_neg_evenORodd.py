num = int(input("Enter any number :"))
if  num == 0  :
    print("it's a zero !") 
elif num > 0 and num % 2 == 0 :
    print("Number is positive and an even number !")
elif num > 0 and num % 2 != 0 :
    print("Number is positive and an odd number !")
elif num < 0 and  num % 2 == 0:
    print("Number is negative and an even number!")
else :
    print("Number is negative and odd number !")