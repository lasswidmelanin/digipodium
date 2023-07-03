from turtle import *
pensize(4)
bgcolor("black")

for i in range(5):
    pencolor('green')
    fd(100)
    rt(360/5)
    for i in range(5):
        pencolor('yellow')
        fd(50)
        rt(360/5)
hideturtle()
mainloop()