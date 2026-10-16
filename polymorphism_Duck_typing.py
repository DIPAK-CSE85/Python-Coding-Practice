class college:
    def student(self):
        print("learn advance subjects")
    def classes(self):
        print("classes are big and use a smart screen for writting")
class school:
    def student(self):
        print("learn basic subjects")
    def classes(self):
        print("classes are small and use a normal board for writting")
def display(a):
    a.student()
    a.classes()    
c1=college()
c2=school()
display(c2)
