# my method (its very large, easy method given below this program)
size=input("what size of pizza you want?(small,meddium,large)=")
bill=0
if(size=="small"):
    print("price of small pizza is 100rs")
    pre=input("do you want preprones?(yes/no)=")
    if(pre=="yes"):
        print("you required  extra 30rs for preprones")
        cheese=input("do you want chess?(yes/no)=")
        if(cheese=="yes"):
            print("you required extra 20rs for cheese")
            bill=100+30+20
        else:
            bill=100+30
    else:
        cheese=input("do you want chess(yes/no)?=")
        if(cheese=="yes"):
            print("you required extra 20rs for cheese")
            bill=100+20
        else:
            bill=100

        
elif(size=="meddium"):
    print("price of meddium pizza is 200rs")
    pre=input("do you want prepronoes(yes/no)?=")
    if(pre=="yes"):
        print("you required  extra 50rs for preprones")
        cheese=input("do you want chess(yes/no)?=")
        if(cheese=="yes"):
            print("you required extra 20rs for cheese")
            bill=200+50+20
        else:
            bill=200+50
    else:
        cheese=input("do you want chess(yes/no)?=")
        if(cheese=="yes"):
            print("you required extra 20rs for cheese")
            bill=200+20
        else:
            bill=200
elif(size=="large"):
    print("prize of large pizza is 300rs")
    pre=input("do you want prepronoes(yes/no)?=")
    if(pre=="yes"):
        print("you required  extra 50rs for preprones")
        cheese=input("do you want chess(yes/no)?=")
        if(cheese=="yes"):
            print("you required extra 20rs for cheese")
            bill=300+50+20
        else:
            bill=300+50
    else:
        cheese=input("do you want chess(yes/no)?=")
        if(cheese=="yes"):
            print("you required extra 20rs for cheese")
            bill=300+20
        else:
            bill=300            
else:
    print("sorry!your enter size is not found, please try agin")    
print("total bill is=",bill)   


# simple method
size=(input("what size of pizza you want?(small/meddium/large)"))
bill=0
if(size=="small"):
    print("price of small pizza is 100rs")
    bill+=100
elif(size=="meddium"):
    print("price of meddium pizza is 200rs")
    bill+=200
elif(size=="large"):
    print("price of large pizza is 300rs")
    bill+=300
else:
    print("sorry!your enter size is not found, please try agin")    

prepproni=input("do you want prepproni?(yes/no)=")
if(prepproni=="yes"):
    if(size=="small"):
        bill+=30
    else:
        bill+=50
cheese=input("do you want extra cheese?(yess/no)=")
if(cheese=="yes"):
    bill+=20
print("total bill is=",bill)


    



