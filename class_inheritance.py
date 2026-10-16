# inheritance means copy or access the attributes ands method of parent,base or super class in the child,derived orsub class 
class human:
    def __init__(self,mark):
        self.num_eyes=2
        self.num_nose=1
        self.num_hands=2
        self.m=mark
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class male(human):
    def __init__(self,name,m):
        super().__init__(m)
        self.name=name
    def work(self):
        super().work()
        print("work is done")
    def display(self):     
        print(f"my name is {self.name} and i got a {self.m} marks in DMGT")
male_1=male("dipak",49)
male_1.eat()
male_1.work()
print(male_1.num_nose)
print(male_1.num_eyes)
print(male_1.num_hands)
print(f"Total marks is={male_1.m}")
male_1.display()




    