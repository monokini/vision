import turtle

class Quadrat:

    def __init__(self,xPos,yPos,xMin,xMax,yMin,yMax,size,angle,color):
        self.__xPos = xPos
        self.__yPos = yPos
        self.__xMin = xMin
        self.__xMax = xMax
        self.__yMin = yMin
        self.__yMax = yMax
        self.__size = size
        self.__angle = angle
        self.__turtle = turtle.Turtle()
        self.__turtle.shape("square")
        self.__turtle.color(color)
        self.__turtle.shapesize(size)
        self.__turtle.speed(-1)
        self.__stampID = 0
        #store values for reset position
        self.__angle_initValue = angle
        self.__xPos_initValue = xPos
        self.__yPos_initValue = yPos

    def __del__(self):
        self.clearStamp()

    @property
    def x(self):
        return self.__xPos

    @property
    def y(self):
        return self.__yPos

    @property
    def angle(self):
        return round(self.__angle,1)
    
    def moveX(self,value):
        if value == 0:
            return
        
        if value > 0:
            if self.__xPos + self.__size/2 + value > self.__xMax:
                return
        else:
            if self.__xPos - self.__size/2 - value < self.__xMin:
                return
            
        self.__xPos += value
        self.stamp()

    def moveY(self,value):
        if value == 0:
            return

        if value > 0:
            if self.__yPos + self.__size/2 + value > self.__yMax:
                return
        else:
            if self.__yPos - self.__size/2 - value < self.__yMin:
                return
        
        self.__yPos += value
        self.stamp()

    def rotate(self,value):
        if value == 0:
            return
        self.__angle += value
        self.stamp()

    def resetPosition(self):
        self.__angle = self.__angle_initValue
        self.__xPos = self.__xPos_initValue
        self.__yPos = self.__yPos_initValue
        self.stamp()
    
    def clearStamp(self):
        if self.__stampID > 0:
            self.__turtle.clearstamp(self.__stampID)
            self.__stampID = 0
            
    def stamp(self):
        self.clearStamp()
        self.__turtle.penup()
        self.__turtle.setpos(self.__xPos,self.__yPos) 
        self.__turtle.setheading(self.__angle)
        self.__turtle.pendown()
        self.__stampID = self.__turtle.stamp()


class Label:

    def __init__(self,xPos,yPos,color):
        self.__xPos = xPos
        self.__yPos = yPos
        self.__color = color
        self.__turtle = turtle.Turtle()
        self.__turtle.shape("square")
        self.__turtle.color(color)
        self.__turtle.speed(-1)
        self.__turtle.width(30)
        self.__turtle.setpos(xPos,yPos)

    def __del__(self):
        self.clearText()

    def writeText(self,text):
        self.clearText()
        self.__turtle.write(text,font=('Arial',15,'bold'))

    def clearText(self):
        self.__turtle.clear()
        #self.__turtle.undo()
    
