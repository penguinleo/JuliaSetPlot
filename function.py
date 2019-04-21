from decimal import *
import cmath as cm
def function(x,c):
    getcontext().prec = 50

    y = x*x + c
    y_radius,y_radians = cm.polar(y)
    x_radius,x_radians = cm.polar(x)
    # dx = Decimal(y_radius) - Decimal(x_radius)
    dx = y_radius - x_radius
    return y,dx
    pass