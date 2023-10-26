import turtle
import keyboard
import sys
from figures import Quadrat, Label
objSize = 10
objLeftX = -200
objDistance = 300

screen = turtle.Screen()
screen.bgcolor('dark gray')
screen.setup(width=1024, height=768, startx=None, starty=None)
turtle.setworldcoordinates(-512,-384,512,384)
screen.title("Vision test version 0.1")
screen.tracer(0, 0)

def move_left():
    objRight.moveX(-1)
    showCoordinates()
    
def move_right():
    objRight.moveX(1)
    showCoordinates()

def move_up():
    objRight.moveY(1)
    showCoordinates()

def move_down():
    objRight.moveY(-1)
    showCoordinates()

def turn_left():
    objRight.rotate(0.1)
    showCoordinates()

def turn_right():
    objRight.rotate(-0.1)
    showCoordinates()

def resetPosition():
    objRight.resetPosition()
    showCoordinates()

def showCoordinates():
    objLabel.writeText("x="+str(objRight.x)+" y=" + str(objRight.y) + " angle=" + str(objRight.angle))
    
def escape():
    global objRight
    global objLeft
    del objRight
    del objLeft
    screen.bye()


# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "4")
screen.onkeypress(move_right, "6")
screen.onkeypress(move_up, "8")
screen.onkeypress(move_down, "2")
screen.onkeypress(turn_right, "9")
screen.onkeypress(turn_left, "3")
screen.onkeypress(resetPosition, "5")
screen.onkeypress(escape, "Escape")

objLeft = Quadrat(objLeftX,100,-300,300,-300,300,objSize,0.0,'red')
objLeft.stamp()
objRight = Quadrat(objLeftX+objDistance,100,-300,300,-300,300,objSize,0.0,'green')
objRight.stamp()
objLabel = Label(-300,-300,'black')
showCoordinates()

turtle.mainloop()



