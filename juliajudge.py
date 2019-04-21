import math as ma   
import cmath as cm 
import numpy as np 
from decimal import *
from function import function
import matplotlib.pyplot as plt 
def juliajudge(x=complex(0.5,1),c=0,t = 50):
    y=[]
    dx_temp = []
    flag = 1   # iteration flag
    index = 0
    temp, dx = function(x,c)
    radius, radian = cm.polar(temp)
    # print('index',index,'the function input:',x,c,'result',temp,'the dx:',dx,ma.fabs(dx))
    while  (index < t) & (radius < 2):
        y.append(temp)
        dx_temp.append(dx)
        temp,dx = function(y[index],c)
        # print('index',index,'the function input:',y[index],c,'result',temp,'dx',dx)
        radius, radian = cm.polar(temp)
        index = index + 1
        pass
    if radius > 2:
        result = 0
        # print('it is not in the julia set:',x,'iteration times:',index)
        pass
    else:
        result = 1;
        # print('find a julia set value:',x,'iteration times:',index)
        pass

    # plt.figure(1)
    # plt.subplot(121)
    # plt.plot(dx_temp,'r*-')
    # # plt.hold()
    # plt.xlabel('times')
    # plt.ylabel('dx')
    # plt.title('the dx trend')
    # plt.subplot(122)
    # plt.plot(y,'y*--')
    # plt.xlabel('times')
    # plt.ylabel('y')
    # plt.title('the y trend')
    # # plt.gridon()

    # plt.show()
    return result, index
    pass