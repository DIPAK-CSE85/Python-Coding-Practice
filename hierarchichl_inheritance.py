class College:
    def __init__(self,name,roll,mark):
        self.num_head=1
        self.name=name
        self.roll=roll
        self.mark=mark
    def room(self):
        print("There are so many room available in college")
class teacher(College):
    def __init__(self,name_p,roll_p,mark_p):
        College.__init__(self,name_p,roll_p,mark_p)
    def lecture(self):
        print("each teacher can teach one subject to each class")
class senior(College):
    def __init__(self,name_d,roll_d,mark_d):
        super().__init__(name_d,roll_d,mark_d)
        self.number=9637671522
    def learn(self):
        print("one student can learn more then 5 subject in each sem")
class junior(College):
    def __init__(self,name_m,roll_m,mark_m):
        super().__init__(name_m,roll_m,mark_m)
    def new(self):
        print("junior are new student in the college")
    def room(self):
        print("new room are available for juniors")    
senior_1=senior("dipak",16,49)
teacher_1=teacher("pranay",456,65)
senior_1.room()
teacher_1.room()
print(senior_1.num_head)
print(teacher_1.num_head)
print(senior_1.number)
print("object class data=")
print(senior_1.name)
print(teacher_1.name)
print(senior_1.roll)
print(teacher_1.roll)
print(senior_1.mark)
print(teacher_1.mark)
junior_1=junior("mandar",234,55)
junior_1.room()



 