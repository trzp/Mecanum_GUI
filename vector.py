import numpy as np
import math

"""
author:mrtang
date:2017.7
version:1.0
email:mrtang@nudt.edu.cn
"""

def isNum(value):
    try:
        value + 1
        return True
    except:
        return False

class vector2D:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
    
    def __add__(self,other):
        return vector2D(self.X+other.X,self.Y+other.Y)

    def __sub__(self,other):
        return vector2D(self.X-other.X,self.Y-other.Y)

    def __mul__(self,other):
        if isinstance(other,vector2D):  return self.X*other.X+self.Y+other.Y
        elif isNum(other):              return vector2D(self.X*other,self.Y*other)
        else:raise TypeError,'unrecgnized data type. vedctor2D and num is supportted.'

    @property
    def Len(self):
        return math.sqrt(self.X**2+self.Y**2)

    @property
    def Angle(self):
        if self.Len == 0:   self.Len = 0.00000000001
        return np.pi*(1-np.sign(self.Y))+np.arccos(self.X/self.Len)*np.sign(self.Y)