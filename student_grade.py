marks = int(input("Enter your marks to check your grade :"))
if marks >= 90 and marks <=100 :
    print("you're passed with grade A !")
elif marks >= 80 and marks <= 89:
    print("you're passed with  grade B !")
elif marks >= 70 and marks <= 79 :
    print("you're passed with grade C !")
elif marks >= 60 and marks <= 69 :
    print("you're passed with grade D !")
elif marks <60 :
    print(" you're passed with grade F !")
else :
    print("incorrect input !!")