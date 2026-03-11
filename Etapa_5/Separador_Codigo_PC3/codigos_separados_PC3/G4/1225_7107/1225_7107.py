from numpy import *
from math import *

x = array(eval(input()))
d = 0
m = sum(x)/size(x)

for i in range(size(x)):
	
	d = d + (x[i] - m) ** 2
	
d = d / (size(x) - 1)
d = sqrt(d)

print(round(d, 3))