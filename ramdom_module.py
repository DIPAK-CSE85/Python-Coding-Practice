import random
a=random.randint(1,5)   #1<=x<=5  (1 and 5 include)
print(a)
b=random.randrange(1,3)    #1<=x<3 (3 not include)
print(b)
c=random.random()     #0.0<=x<1.0  (1.0 not include  ,only floating values)
print(c)
d=random.uniform(2,6)    #2<x<6  (only floating values)
print(d)

l=[23,67,54,12,3,4,6,90,21,22,44,66]
z=random.choice(l)        #its print the random value from list
print(z)
random.shuffle(l)    #it change the order only
print(l)