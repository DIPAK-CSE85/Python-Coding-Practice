import os
print("*****WELCOME TO SILENT AUCTION PROGRAM*****")
silent_data={}
def program():
    name=input("Enter bidder name=")
    bit_price=int(input("enter the bit price="))
    silent_data[name]=bit_price
    next_bit=input("next bidder are available?(yes,no)=")
    if(next_bit=='yes'):
        os.system('cls')
        program()
    else:
        price_list=[]
        for values in silent_data.values():
            price_list.append(values)   
        maximum=max(price_list)
        for key in silent_data:
            if(silent_data[key]==maximum):
                print(f"here is the list of all bidders {silent_data}")
                print(f"winner is {key} and highest price {maximum}")
program()                