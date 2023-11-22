from turtle import *

pensize(2)
speed('fastest')
bgcolor('black')
pencolor('yellow')
width(2)
for i in range(6):
    lt(60)
    fd(100)
    for i in range(6):
        lt(60)
        fd(50) 
        fillcolor('blue')  
        begin_fill()
    circle(90,60)             
hideturtle()
mainloop()        
