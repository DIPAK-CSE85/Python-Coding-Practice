import random
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j',
         'k','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P',
         'A','S','D','F','G','H','J','K','L','Z','X','V','B','N','M']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['~','!','@','#','$','%','^','&','*']
n_letters=int(input("how many letters you want to in your passward="))
n_numbers=int(input("how many numbers you want to in your passward="))
n_symbols=int(input("how many symbils you want to in your passward="))
passward=" "       #string
for i in range(1,n_letters+1):
    char=random.choice(letters)
    passward+=char
for i in range(1,n_numbers+1):
    num=random.choice(numbers)
    passward=passward+num  
for i in range(1,n_symbols+1):
    sym=random.choice(symbols)
    passward=passward+sym          
print("simple passward is=",passward)
list=list(passward)    #typecasting from string to list
random.shuffle(list)    #used shuffle function 
passward=""       #string for converting list into string
for i in list:
    passward=passward+i
print("strong passward is=",passward)    





#second method is given below

import random
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','V','B','N','M']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*']
n_letters=int(input("how many letters you want to in your passward="))
n_numbers=int(input("how many numbers you want to in your passward="))
n_symbols=int(input("how many symbils you want to in your passward="))
passward_list=[]     #list
for i in range(0,n_letters):
    char=random.choice(letters)
    passward_list+=char
for i in range(1,n_numbers+1):
    num=random.choice(numbers)
    passward_list+=num  
for i in range(1,n_symbols+1):
    sym=random.choice(symbols)
    passward_list+=sym          
print("simple passward is=",passward)
random.shuffle(passward_list)      #used shuffle function
passward=""            #string for converting list into string
for i in passward_list:
    passward=passward+i
print("strong passward is=",passward)  