print("here we're checking a valid triangle by it's sides ")
a1 = int(input("Enter first side"))
a2 = int(input("Enter second side"))
a3 = int(input("Enter third side"))
if a1 + a2 > a3  or a2 + a3 > a1 or a1 + a3 > a2 : 
    print("it's a valid triangle !")
    if ( a1 == a2 == a3) : 
        print("it's a equiliteral triangle !")   
    if  (a1 == a2 or a2 == a3 or a1 == a3) :
        print("it's a isosceles triangle !")
    else :
        print("it's scalene triangle !")
else :
    print("it's not a valid triangle !")
