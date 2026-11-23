eng = float(input("Enter marks of english :"))
hin = float(input("Enter marks of hindi :"))
mat = float(input("Enter marks of mathematics  :"))
avg = (eng + hin + mat)/ 3 
if avg >= 75 :
    print("Distinction !")
elif avg >= 60 and avg <= 74 :
    print("First Class !")
elif avg >= 40 and avg <= 59 :
    print("Second Class !")
elif avg < 40 and avg > 0 :
    print("Failed !")
else :
    print("invalid input ")