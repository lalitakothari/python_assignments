age = int(input("Enter your age :"))
if age <= 1 and age >= 0 :
    print(" you're an Infant !")
elif age <= 4 and age >= 2 :
    print(" you're a Toddler !")
elif age <= 12 and age >= 5 :
    print(" you're a Child !")
elif age <= 19 and age >= 13 :
    print(" you're a teenager !")
elif age <= 59 and age >= 20 :
    print(" you're an Adult !")
elif age >= 60  :
    print(" you're a Senior !")
else :
    print("invalid Input !")