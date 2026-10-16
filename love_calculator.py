name1=input("what is your name?=")
name2=input("what ios your girl/boy friend name?=")
join=name1+name2
lower=join.lower()
t=lower.count('t')
r=lower.count('r')
u=lower.count('u')
e=lower.count('e')
true=t+r+u+e

l=lower.count('l')
o=lower.count('o')
v=lower.count('v')
e=lower.count('e')
love=l+o+v+e
love_score=int(str(true)+str(love))
if(love_score<10)or(love_score>90):
    print(f"your love score is{love_score} and you go together like coke and mentos")
elif(love_score>=40 and love_score<=50):
    print(f"your score is {love_score} and you are alright together")
else:
    print(f"your love score is{love_score}")
