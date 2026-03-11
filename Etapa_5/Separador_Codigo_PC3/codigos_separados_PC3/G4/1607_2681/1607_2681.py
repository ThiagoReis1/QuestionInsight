from numpy import *
from math import *
ap = array(eval(input("andares que o elevador parou: ")))
d=0
i = 0

while i < (size(ap)-1):
	d += abs((ap[i+1] - ap[i] )*3)
	
	i+=1
print(d)
