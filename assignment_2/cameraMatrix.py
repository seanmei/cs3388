import operator
from math import *
from re import T
import numpy as np
from matrix import matrix

class cameraMatrix:

    def __init__(self,window,UP,E,G,nearPlane=10.0,farPlane=50.0,theta=90.0):
        self.__UP = UP.normalize()
        self.__E = E
        self.__G = G
        self.__np = nearPlane
        self.__fp = farPlane
        self.__width = window.getWidth()
        self.__height = window.getHeight()
        self.__theta = theta
        self.__aspect = self.__width/self.__height
        self.__npHeight = self.__np*(pi/180.0*self.__theta/2.0)
        self.__npWidth = self.__npHeight*self.__aspect

        Mp = self.__setMp(self.__np,farPlane)
        T1 = self.__setT1(self.__np,self.__theta,self.__aspect)
        S1 = self.__setS1(self.__np,self.__theta,self.__aspect)
        T2 = self.__setT2()
        S2 = self.__setS2(self.__width,self.__height)
        W2 = self.__setW2(self.__height)

        self.__N = (self.__E - self.__G).removeRow(3).normalize()
        self.__U = self.__UP.removeRow(3).crossProduct(self.__N).normalize()
        self.__V = self.__N.crossProduct(self.__U)

        self.__Mv = self.__setMv(self.__U,self.__V,self.__N,self.__E)
        self.__C = W2*S2*T2*S1*T1*Mp
        self.__M = self.__C*self.__Mv

    def __setMv(self,U,V,N,E): # Mv = (TR)^-1 R^ -1 T ^-1 
        #Complete this method
    

        #remove row that not needed 
        Mv = matrix(np.identity((4))) #create matrix 

        #remove row 3 that is not needed
        E2 = E.removeRow(3).transpose() #tranpose E so that it has the correct dimmensions 

        #calculate values and get firts value to insert in matrix 
        VV = (-E2*V).get(0,0)
        UU = (-E2*U).get(0,0)
        NN = (-E2*N).get(0,0)


        #enter values of matrix each matrix u,v,n 1 by 1 according to definition 
        #row 0
        Mv.set(0, 0, U.get(0, 0)) 
        Mv.set(0, 1, U.get(1, 0))
        Mv.set(0, 2, U.get(2, 0))
        
        #row 1 
        Mv.set(1, 0, V.get(0, 0))
        Mv.set(1, 1, V.get(1, 0))
        Mv.set(1, 2, V.get(2, 0))

        #row 2
        Mv.set(2, 0, N.get(0, 0))
        Mv.set(2, 1, N.get(1, 0))
        Mv.set(2, 2, N.get(2, 0))

        #row 3
        Mv.set(3,0,0)
        Mv.set(3,1,0)
        Mv.set(3,2,0)
        Mv.set(3, 3, 1)
        
        #insert the calcualte values 
        Mv.set(0, 3, UU)
        Mv.set(1, 3, VV)
        Mv.set(2, 3, NN)
        

        return Mv

    def __setMp(self,nearPlane,farPlane):
        #easier to read variables 
        N = nearPlane  
        F = farPlane 

        a = -(F + N) / (F-N) #definition 
        b = -(2*F*N) / (F-N)  

        #create mp array using numpy and fill values of mp
        mp = np.array([
            [N,0,0,0],
            [0,N,0,0],
            [0,0,a,b],
            [0,0,-1,0]
            ])
        return matrix(mp)

       
    def __setT1(self,nearPlane,theta,aspect):
        #assign value
        N = nearPlane 
        A = aspect 

        #calculate values of t,l,b for T1
        t = N*tan((pi/180)*(theta/2))
        b = -t 
        r = A*t
        l = -r 

        #some math for element in matrix 
        i = -(r+l)/2
        j = -(t+b)/2


        #create matrix with values 
        t1 = np.array([
            [1,0,0,i],
            [0,1,0,j],
            [0,0,1,0],
            [0,0,0,1]
        ])
        return matrix(t1)
        
    def __setS1(self,nearPlane,theta,aspect):
        #assign value
        N = nearPlane 
        A = aspect 

        #calculate values of t,l,b for T1
        t = N*tan((pi/180)*(theta/2))
        b = -t 
        r = A*t
        l = -r 

        #some math for elements in the matrix 
        i = 2/(r-l)
        j = 2/(t-b)

        #create matrix with values 
        s1 = np.array([
            [i,0,0,0],
            [0,j,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ])
        
        return matrix(s1)


        
    def __setT2(self):
        #t2 matrix 
        t2 = np.array([
            [1,0,0,1],
            [0,1,0,1],
            [0,0,1,0],
            [0,0,0,1]
        ])
        return matrix(t2)
        
    def __setS2(self,width,height):
        #assign value
        w = width 
        h = height 

        #create matix 
        s2 = np.array([
            [(w/2),0,0,0],
            [0,(h/2),0,0],
            [0,0,1,0],
            [0,0,0,1]
            ])
        return matrix(s2)
        
    def __setW2(self,height):
        #assign value
        h = height 

        #create matix 
        w2 = np.array([
            [1,0,0,0],
            [0,-1,0,h],
            [0,0,1,0],
            [0,0,0,1]
        ])
        return matrix(w2)
        
    def worldToViewingCoordinates(self,P):
        return self.__Mv*P

    def worldToImageCoordinates(self,P):
        return self.__M*P

    def worldToPixelCoordinates(self,P):
        return self.__M*P.scalarMultiply(1.0/(self.__M*P).get(3,0))

    def viewingToImageCoordinates(self,P):
        return self.__C*P

    def viewingToPixelCoordinates(self,P):
        return self.__C*P.scalarMultiply(1.0/(self.__C*P).get(3,0))

    def imageToPixelCoordinates(self,P):
        return P.scalarMultiply(1.0/P.get(3,0))

    def getUP(self):
        return self.__UP

    def getU(self):
        return self.__U

    def getV(self):
        return self.__V

    def getN(self):
        return self.__N

    def getE(self):
        return self.__E

    def getG(self):
        return self.__G

    def getMv(self):
        return self.__Mv

    def getC(self):
        return self.__C

    def getM(self):
        return self.__M

    def getNp(self):
        return self.__np

    def getFp(self):
        return self.__fp

    def getTheta(self):
        return self.__theta

    def getAspect(self):
        return self.__aspect

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getNpHeight(self):
        return self.__npHeight

    def getNpWidth(self):
        return self.__npWidth