from numpy import*
from math import*
ae = array(eval(input()))
d = 3
sa = size(ae)
i = 0
dt = 0
while(i < sa-1):
	de = abs(ae[i+1]-ae[i])*3
	dt = dt + de
	i = i+1
print(dt)