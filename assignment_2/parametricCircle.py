from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricCircle(parametricObject):


    def __init__(self, #set key values for circle 
                 T=matrix(np.identity(4)), radius = 10, color=(0,0,0),
                 reflectance=(0.0,0.0,0.0),
                 uRange=(0.0, 2*pi),
                 vRange=(0.0, pi),
                 uvDelta=(1.0/10.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta) #pass values to create parametric object 
        self.__radius = radius
    

    def getPoint(self,u,v):
        #Circle matrix values based on definition
        P = np.array([
            [self.__radius*cos(v)*u],
            [self.__radius*sin(v)*u],
            [0],
            [1]
        ])
        return matrix(P)
 