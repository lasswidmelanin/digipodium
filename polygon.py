from turtle import *
def square():
   for i in range(4):
     forward(100)
     right(90)

def pentagon():
   for in range(5):
     forward(100) 
     right(72)
      
# for i in range(5):
# fd(200)
#   pentagon()
#   right(72)

square()
pentagon()
goto(200)
square()
pentagon()

hideturtle()
mainloop()