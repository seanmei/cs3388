import operator
from PIL import Image


#-------graphicsWindow--------
 #Implementation of Bresenham's integer line algorithm
# Author: Sean Mei 
  #Date of creation: Jan 28, 2022
  #Purpose: Use Bresenham's integer line algorithm to draw lines connecting points from testAssignment.py

class graphicsWindow:
   


    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    
  # -------------------drawLine -------------
  # Author: Sean Mei 
  #Date of creation: Jan 28, 2022
  #Purpose: This function reeives 2 points from testAssignment.py. Before being able to
  # draw the lines using the Bresenham's integer line algorithm we must fist sort the points 
  #into 4 casses based on the direction of the slope. This function will correctly call drawLineFlat 
  #drawLine steep based on the points 
  #Parameters:
  #self refers to an instance of the class 
  #point1 - first point - inpput 
  #point2 -  second point - input 
  #color -  color of the  points that will be drawn input
    
    def drawLine(self,point1,point2,color): 


        # retreive values from the matrix of given points 
        x1 = (point1.get(0,0)) 
        x2 = (point2.get(0,0)) 
        y1 = (point1.get(1,0)) 
        y2 = (point2.get(1,0)) 
        
        #sorts the given points into 4 different cases based on the slop of the line created by the 2 points 
        if abs(x2-x1) > abs(y2-y1): #case of line with steep slope (|m| >= 1 )
            if x2 < x1:  # case for drawing a line with a steep slope (i.e., greater than 1)
                self.drawLineFlat(x2, y2, x1, y1, color)
            else:                               
                self.drawLineFlat(x1, y1, x2, y2, color)
        else:  # case for dawing line with flat slope (-1<m<1)
            if y2 < y1:  
                self.drawLineSteep(x2, y2, x1, y1, color)
            else: #flip points line in opisite direction 
                self.drawLineSteep(x1, y1, x2, y2, color)



  # -------------------drawLineFlat -------------
  # Author: Sean Mei 
  #Date of creation: Jan 28, 2022
  #Purpose: This function implements Bresenham's integer line algorithm on lines with a gradual slope 
  #By calling the drawPoint and using the alorithm to select which points to select betweent the 2 given points 
  #Parameters:
  #self refers to an instance of the class 
  #x1 - valu of x of the first point - input 
  #x2 - value of x in the second point - input 
  #y1 - value of y in the first point - input 
  #y2 - value of y in the second point - input 
  #color - color of the line - input
    
    def drawLineFlat(self, x1, y1,  x2, y2, color): 
        dy = y2 - y1        # change in y
        step = 1
        pi = None

        self.drawPoint((x1,y1), color) #draw first point 

        if dy < 0: # check the direction of y 
            dy *= -1 #flip direction if needed
            step *= -1  #increment in other direction

        for i in range(int(x1), int(x2)): #find next point by picking the closeset one 
            if i == x1:
                dx = x2-x1 #change in x 
                pi = 2*dy-dx #set initial value 
            else:
                if pi < 0:
                    pi =pi + 2*dy 
                else:
                    pi = pi + 2*dy - 2*dx
                    y1= y1 + step
                x1 = x1 + 1
                self.__image[x1, y1] = color

      # -------------------drawLineSteep -------------
  # Author: Sean Mei 
  #Date of creation: Jan 28, 2022
  #Purpose: This function implements Bresenham's integer line algorithm on lines with a stpeep slope 
  #By calling the drawPoint and using the alorithm to select which points to select betweent the 2 given points 
  #Parameters:
  #self refers to an instance of the class 
  #x1 - valu of x of the first point - input 
  #x2 - value of x in the second point - input 
  #y1 - value of y in the first point - input 
  #y2 - value of y in the second point - input 
  #color - color of the line - input
                
    def drawLineSteep(self, x1, y1,  x2, y2, color): 
        dx = x2 - x1       # change in y
        step = 1
        pi = None

        self.drawPoint((x1,y1), color) #draw point 


        if dx < 0: # check the direction of y 
            dx *= -1 #change direction 
            step *= -1

        for i in range(int(y1), int(y2)): #find next point by fiding distance to closest next point
            if i == y1:
                dy = y2 - y1
                pi = 2*dx-dy #set intial value 
            else:
                if(pi < 0):
                    pi = pi + 2*dx 
                else:
                    pi = pi + 2*dx - 2*dy
                    x1= x1 + step
                y1 = y1 + 1
                self.__image[x1, y1] = color
            

        

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height