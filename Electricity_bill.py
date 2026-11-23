previous_readin = float(input("enter previously reading :"))
current_reading = float(input("enter currently reading :"))
Units_Consumed =  current_reading - previous_readin
print("units consumed =" ,Units_Consumed)

if Units_Consumed <= 100 :
    bill = Units_Consumed * 5
    print("total electricity bill is :", bill)
elif Units_Consumed <= 200 :
    bill= (100 * 5) +(Units_Consumed - 100) * 7
    print("total electricity bill is :", bill)
elif Units_Consumed > 200 :
    bill = ((Units_Consumed - 200)*10 +(100 * 5) + (100 * 7))
    print("total electricity bill is :",bill)
else : 
    print("something went wrong !")

 