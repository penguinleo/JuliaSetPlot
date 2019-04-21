import math as ma   
import cmath as cm 
import numpy as np 
from decimal import *
from function import function
from juliajudge import juliajudge
from matrix2array import matrix2array
getcontext().prec = 50
def juliasearch(x=[[complex(0,0)]],c=-0.75,t=50):
    x_row_len = len(x)
    x_col_len = len(x)
    x_array = matrix2array(x)
    x_len = len(x_array)
    y = []
    g = []
    for i in range(0,x_len):
        result,index = juliajudge(x_array[i],c,t)
        g.append(index)
        if result == 1:
            y.append(x_array[i])
            pass
        pass
    pass
    print('find julia set value:',len(y))
    return y,g
    pass