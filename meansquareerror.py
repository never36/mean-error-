from statistics import mean
import numpy as np
import plot as plot

x1=0*0
y1=1*0.8+1*0.8
x2=2*2.2+2*2.2+2*2.2+2*2.2
y2=3*2.8+3*2.8+2*2.8+3*2.8+3*2.8
x3=4*4.5+4*4.5+4*4.5+4*4.5+4*4.5+4*4.5

mean=x1+y1+x2+y2+x3

average=mean/5


print (average)

def slope(x1, y1, x2, y2, x3):
    return (float)(y2-y1)/(x3-x2-x1)

print ("Slope is:", slope(x1, y1, x2, y2, x3))