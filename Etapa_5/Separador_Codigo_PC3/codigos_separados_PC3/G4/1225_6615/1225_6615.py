from numpy import * 
from math import *
x = array(eval(input("vetor: ")))

m = sum(x)/size(x)

d = 0
for i in range(size(x)): 
	d = d + ((x[i]-m)**2)/(size(x)-1)

print(round(sqrt(d),3))
