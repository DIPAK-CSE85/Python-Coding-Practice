class human:
    def __init__(self,name):
         self.name=name
         self.num_eyes=2
    def eat(self):
        print("I  can eat")
    def work(self):
        print("I can work")
class male():
    def __init__(self,roll):
         self.roll=roll
         self.num_head=1
    def apple(self):
        print("I can eat apple")
    def ruppes(self):
            print("I have 200rs")
    def work(self):
          print("I am bussy in my work")
class man(human,male):
     def __init__(self,name,r):
          human.__init__(self,name)
          male.__init__(self,r)
          self.number=90
     def run(self):
          print("I can rum")
man_1=man("dipak",16)
man_1.apple()  
man_1.work()      
human.work(man_1)
male.work(man_1)   
man_1.eat()   
man_1.run()       
print(f"number of eyes={man_1.num_eyes}")
print(f"number of head={man_1.num_head}")
print(f"name is={man_1.name}")
print(f"roll number is={man_1.roll}")
print(f"number is={man_1.number}")