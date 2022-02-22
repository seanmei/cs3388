from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricCylinder(parametricObject):


    def __init__(self, #key values for cylinder  
                 T=matrix(np.identity(4)), height = 20.0, radius = 10.0, color=(0,0,0),
                 reflectance=(0.0,0.0,0.0),
                 uRange=(0.0, 1),
                 vRange=(0.0, 2*pi),
                 uvDelta=(1.0/10.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta) #creat parametric object 
        self.__height = height
        self.__radius = radius


    def getPoint(self,u,v):
        #cylinder matrix values by definition 
        P = np.array([
            [self.__radius*sin(v)],
            [self.__radius*cos(v)],
            [self.__height*u],
            [1]
        ])
        return matrix(P)
 