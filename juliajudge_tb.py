import math as ma   
import cmath as cm 
import numpy as np 
from decimal import *
from function import function
from juliajudge import juliajudge
getcontext().prec = 50

x = Decimal(1.5)
# x = complex(-1.8037,0.12448)
x = 1.501
juliajudge(x,-0.75,500)

