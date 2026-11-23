print("1. kilometers to miles : \n 2. Celsius to fehrenheit : \n 3. kilogram to pounds :")
choice = int(input(" Enter number of your choice :"))
value = float(input(" Enter a value to convert :"))

if choice == 1 :
    miles = value * 0.621371
    print( value," km after converted in miles is =" , miles)

elif choice == 2 :
    feh = ((value * 9) / 5 + 32)
    print( value,"celsius after converted in fehrenheit is =" , feh)

elif choice == 3 :
    pounds = value * 2.20462 
    print(value,"kg after converted in pounds is =" , pounds)

else :
    print("invalid choice ")