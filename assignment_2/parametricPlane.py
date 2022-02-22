from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricPlane(parametricObject):


    def __init__(self, #key values for plane 
                 T=matrix(np.identity(4)),height = 0, width=1.0, color=(0,0,0),
                 reflectance=(0.0,0.0,0.0),
                 uRange=(0.0,1.0),
                 vRange=(0.0,1.0),
                 uvDelta=(0.0,0.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__width = width
        self.__height = height

    def getPoint(self,u,v):
        #plane matrix 
        P = np.array([
            [u*self.__width], #uw
            [v*self.__height], #vh 
            [0],
            [1]
        ])
        return matrix(P)
