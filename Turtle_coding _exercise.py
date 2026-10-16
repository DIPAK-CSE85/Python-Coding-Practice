import turtle
t=turtle.Turtle()
t.shape('arrow')
t.width(2)
n=1
t.speed(150)
for i in range(40):
    def num(n):
        for d in range(2):
            for i in range(n):
                t.pencolor('red')
                t.fd(10)
                t.pencolor('black')
                t.fd(5) 
            t.lt(90)
    num(n)
    n+=1
    
t.screen.mainloop()