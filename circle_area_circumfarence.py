radius=int(input("Enter a radius of a circle="))
class circle_dada:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"Area of a circle is={self.pi*self.radius**2}") 
    def circumfarence(self):
        print(f"circumfarence of a circle is={2*self.pi*self.radius}") 
                  
calculation=circle_dada(radius)
calculation.area()
calculation.circumfarence()

