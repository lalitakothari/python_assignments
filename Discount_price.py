price = int(input("Enter the product price to check discount !"))

if price > 1000 :
    disc_price = price *( 10/100 )
    final_price = price - disc_price
    print("your final price after applying discount is :",final_price)
    
elif 500 < price <= 1000 :
    disc_price = price *(5/100)
    final_price = price - disc_price    
    print("your final price after applying discount is :",final_price )
    
else :
    ("there are no discount !")