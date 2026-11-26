uname = input("enter username :")
password = input("enter password :")
if uname == "admin" :
    if password == "1234" :
        print("you're logged in !")
    else :
        print("incorrect password!")
else :
    print("user not exist try to sign in !")
