
age = int(input("Enter your age: "))
gender = input("Enter your voter identity (M/F): ").upper()

if age >= 18 and (gender == "M" or gender == "F"):
    print("You're eligible to vote!")

elif age < 18 and (gender == "M" or gender == "F"):
    print("Age is not eligible to vote!")

else:
    print("gender not recognized!")
