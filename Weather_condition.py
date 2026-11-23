temp = int(input("Enter the temparature in celsius :"))
if temp < 0 :
    print(" Freezing !")
elif temp > 0 and temp < 15 :
    print(" Cold !")
elif temp >= 16 and temp <= 25 :
    print(" Pleasant!")
elif temp >= 26 and temp <= 35 :
    print(" Warm !")
else :
    print(" Hot !")