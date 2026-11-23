age = int(input("Enter your age :"))
if age < 5 and age > 0 :
    print(" your ticket is Free !")
elif age >= 5 and age <= 12 :
    print(" your ticket price is 100 rs!")
elif age >= 13 and age <= 59 :
    print(" your ticket price is 200 !")
else :
    print(" your ticket price is 120 !")