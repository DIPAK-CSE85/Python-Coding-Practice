import random
import logo
print(logo.design)
print("let me think of a number between 1-50")
random_no=random.randint(1,50)
print(random_no)
choice=input("choose level of deficulty..type 'easy' or'hard':")
if(choice=='hard'):
    attempts=5
else:
    attempts=10
while attempts>0:    
    print(f"you have {attempts} guess remaining to guess the number")
    guess_no=int(input("make a guess="))
    if(random_no==guess_no):
        print(f"your guess number is right,and your answer is {guess_no},you win!") 
        break 
    elif(random_no>guess_no):
        attempts=attempts-1
        print("your guess is TOO low")
        if attempts>0:
            print("guess agin")
        else:
            print("your chance over,you loose!")
    else:
        attempts=attempts-1
        print("your guess is TOO high")
        if attempts>0:
            print("guess agin")
        else:
            print("your chance over,you loose!")


