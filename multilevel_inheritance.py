class human:
    def __init__(self,n):
             self.name=n
             self.num_eyes=2
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can do my work")        
class male(human):
    def __init__(self,roll):
        self.num_hands=2
        self.roll=roll
    def work(self):
        super().work()
        print("I can work")
class man(male): 
    def __init__(self,name,roll):
            human.__init__(self,name)
            male.__init__(self,roll)
            self.num_head=1
    human.work(male)
    #male.work(male)
    def work(self):
         human.work(self)
         male.work(self)
         print("I can code")   
man_1=man("dipak",16)
man_1.eat()
man_1.work() 
print(f"num_of_eyes={man_1.num_eyes}")               
print(man.mro())
print(man_1.name)
print(man_1.roll)