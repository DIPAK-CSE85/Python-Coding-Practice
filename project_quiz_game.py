from quiz_game_dataset import questions
from quiz_game_dataset import options
print("**************************\n WELCOME TO MY QUIZ GAME\n**************************")
def quiz(choice,count,answer):
    global score
    if answer==choice:
        print("your answer is right")
        score+=1
        print(f"your score is={score}/{count}")
    else:
        print("your answer is wrong")
        print(f"your score is={score}/{count}")
score=0
answers=[2,2,2,3,3,2,3,2,2,3,]
for i in range(len(questions)):
    count=i+1
    print(questions[i]["question"])
    for j in range(len(options[i])):
        print(options[i][j])
    choice=int(input("enter your answer from (1,2,3,4)="))  
    quiz(choice,count,answers[i]) 
print("*****THANK YOU*****")    
