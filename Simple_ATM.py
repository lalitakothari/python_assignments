balance = 1000 
print("choose an action to perform : \n  1.Check Current Balance \n 2.Diposite \n 3.Withdraw") 
choice = int(input("Enter selected number to perform action : "))
if choice == 1 :
    print("your current balance is :",balance )
    
elif choice == 2 :
    cash = int(input("Enter the amount for deposite "))
    balance += cash
    print("money deposite successfully !")
    
elif choice == 3  :
    cash = int(input("Enter the amount to withdraw"))
    if cash < balance :
        balance = balance - cash
        print("money withdraw successfully , remaining balance :", balance )
    else :
        print("insufficient balance !")
    
else :
    print("invalid input !") 
                     