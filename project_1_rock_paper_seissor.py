import random
your_choice=input("enter your choice from(rock,paper,secissor=)")
computer_choice=['rock','paper','scissor']
computer_choice1=random.choice(computer_choice)
print("computer choice is=",computer_choice1)
if(your_choice==computer_choice1):
    print("game will tai")
elif(your_choice=='rock'):
    if(computer_choice1=='paper'):
        print('you lose!,because paper cover the rock')
    else:
        print('you win!,because rock break the scissor')
elif(your_choice=='paper'):
    if(computer_choice1=='rock'):
        print("you win!,because paper cover the rock")
    else:
        print("you lose!,because scissor cut the paper")
elif(your_choice=='scissor'):
    if(computer_choice1=='rock'):
        print("you lose!,because rock break the scissor")
    else:
        print("you win!,because scissor cut the paper")
else:
    print("soory! plese try again and enter valid option")        
        