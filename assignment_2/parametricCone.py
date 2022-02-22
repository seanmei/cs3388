from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricCone(parametricObject):


    def __init__(self, #set key values for cone
                 T=matrix(np.identity(4)), height = 20.0, radius = 10.0, color=(0,0,0),
                 reflectance=(0.0,0.0,0.0),
                 uRange=(0.0, 1),
                 vRange=(0.0, 2*pi),
                 uvDelta=(1.0/10.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta) #create parameteirc object 
        self.__height = height
        self.__radius = radius
    


    def getPoint(self,u,v):
        #cone matrix  value by definition 
        P = np.array([
            [(self.__height*(1-u))/self.__height*self.__radius*sin(v)],
            [self.__height*(1-u)/self.__height*self.__radius*cos(v)],
            [self.__height*u],
            [1]
        ])
        return matrix(P)
 