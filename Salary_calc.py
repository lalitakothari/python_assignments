hr= float(input("Enter your working hrs :"))

if hr < 40 :
    salary = hr * 200 
    print("your salary is :",salary)
    
elif hr >= 40 and hr <= 60 :
    salary = ((40 * 200 ) + (hr - 40 )*300)
    print("your salary is :",salary)
    
elif hr > 60 :
    print("overtime limit exceeded !")
    
else :
    print("invalid input !")