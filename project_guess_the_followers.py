import random
import footballers
import cricketers
print("***WELCOME YO HIGHER LOWER GAME***")
count=0
def followers(option,follows_1,follows_2):
    global count
    if(option==1):
        if(follows_1>follows_2):
            print("wwwww")
            count+=1
            return True
        else:
            print("your option is wrong,you lost!")
            return False
    else:
        if(follows_2>follows_1):
            print("aaaa")
            count+=1
            return True
        else:
            print("your option is wrong,you lost!")
            return False
value=True     
while value:
    cricket_p=random.choice(cricketers.cricketers_list)
    football_p=random.choice(footballers.footballers_list)    
    print(f"compair_1={cricket_p['name']},{cricket_p['description']},{cricket_p['country']}")
    print("...VS...")
    print(f"compair_1={football_p['name']},{football_p['description']},{football_p['country']}")        
    follows_1=cricket_p["followers_count_million"]   
    print(follows_1) 
    follows_2=football_p["followers_count_million"] 
    print(follows_2)
    option=int(input("who is more followers?type '1' or '2'="))
    value=followers(option,follows_1,follows_2)
    if(value==True):
        print("your score is=",count)
    