from numpy import*
from math import*

n = array(eval(input("n: ")))
v = 0				
m = ((v[0] ** 1/2) + (v[1] ** 1/2)+ (v[n-1]**1/2)/n ) ** 2
print(round(m,2))