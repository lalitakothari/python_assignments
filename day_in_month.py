month = input("Enter month name to check days in that month : ")
day31 = "january march may july august october december "
day30 = "april june september november "
if month in day31 :
    print(" this month contains 31 days !")
elif month in day30 :
    print(" this month contains 30 days !")
elif month == "february" :
    print ("this is a leap year , this month contains 29 days !" )
else :
    print(" invalid input !")