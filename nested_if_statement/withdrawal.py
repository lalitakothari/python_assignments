balance = 10000
withdraw = int(input("Enter the amount to withdraw :"))
if withdraw > 0 :
    if withdraw % 100 == 0 and withdraw <= balance :
        balance = balance - withdraw
        print(" Money Withdrawal Successfully , your current balance after withdrawal is :",balance)
    else :
        print("can not withdraw money !")
else :
    print("incorrent input !")
