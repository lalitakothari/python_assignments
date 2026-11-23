character = input("Enter any single character here :")
if character >= 'A' and character <= 'Z' :
    print(" It's an uppercase Character !")
elif character >= 'a' and character <= 'z' :
    print(" It's a lowercase Character !")
elif character >= '0' and character <= '9' :
    print(" It's a digit ! ")
else :
    print("It's a special character !")