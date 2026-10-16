import random
import word_list
import hangman_sign
print("welcome to hangman game")
user_choice=random.choice(word_list.words)
print(user_choice)
display=[]
for i in range(len(user_choice)):
    display+="_"
print(display)  
game_over=False 
lives=6
while not game_over:
    other_choice=input("gusse a letter=").lower()
    for i in range(len(user_choice)):
        if(user_choice[i]==other_choice):
            display[i]=other_choice
    print(display)
    if(other_choice not in user_choice):
         lives-=1
         if(lives==0):
             print("you lost!!")
             game_over=True
    if "_" not in display:
         print("you win!!")
         game_over=True
    print(hangman_sign.shape[lives])            
