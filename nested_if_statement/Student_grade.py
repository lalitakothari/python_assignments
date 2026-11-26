marks = int(input("enter your marks :"))
if marks > 0 and marks <= 100 :
    if marks >= 90 :
        print("Grade A !")
    elif marks <= 89 and marks >= 75 :
        print("Grade B !")
    elif marks <= 74 and marks >= 50 : 
        print("Grade C !")
    else :
        print("you're failed !")
else :
    print("invalid marks !")
