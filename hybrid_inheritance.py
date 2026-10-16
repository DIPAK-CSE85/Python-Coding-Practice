class university:
    def __init__(self):
        self.u_name="G H Raisoni skill Teach university,Nagpur"
    def details(self):
        print(f"name of university is={self.u_name}")
class course(university):
    def __init__(self,c_name):
        super().__init__(self)
        self.n_course=c_name  
    def details(self):
        super().details()
        print(f"name of course is={self.n_course}")    
class branch(university):
    def __init__(self,b_name):
        super().__init__()
        self.n_branch=b_name  
    def details(self):
        super().details()
        print(f"name of branch is={self.n_branch}")   
class student(course,branch):
    def __init__(self,s_name,c_name,b_name):
        self.name=s_name
        course.__init__(self,c_name)  
        branch.__init__(self,b_name)
    def details(self):
         print(f"name of student is={self.name}")
         course.details(self)  #first of all go into the course class then by using super go into the branch class(branch next  to course) and access branch name then go into university class and access the u_name and at the end access course name
class faculty(branch):
    def __init__(self,f_name,b_name):
        self.f_name=f_name 
        branch.__init__(self,b_name)
    def details(self):
         print(f"name of faculty is={self.f_name}")
         print(f"name of university is={self.u_name}")   # insted of this used the super().details()
         print(f"name of branch is={self.n_branch}")
student_1=student("dipak","Computer science engineering","CSE") 
student_1.details() 
faculty_1=faculty("Amita","CSE")            
faculty_1.details() 
print(student.mro())
#u=university()        
#u.details()         
#x=course("engineering")        
#x.details()         
#z=branch("CSE")        
#z.details()
