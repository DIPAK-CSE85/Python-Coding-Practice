list=[1,2,3,4,5,6,7,8]
print(len(list))
print(list)
print(dir(int))
class new_length:
    name="dipak sudhakar shivankar"
c1=new_length()
print(len(c1.name)) 


#method overloading
class calculation:
    def sum(self,a,b,c=0):
        return a+b
    #def sum(self,a,b,c):
     #   return a+b+c
c=calculation()   
print(c.sum(12,2)) 
print(c.sum(12,34,56))


#method overriding
class father:
    def sleep(self):
        print("sleeps from 8pm to 5am")
    def eat(self):
        print("eat helthey food every day")
class child(father):
    def sleep(self):
        super().sleep()
        print("sleeps from 11pm to 8am")
        
c=child()
c.sleep()                 