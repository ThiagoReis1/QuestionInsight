from numpy import *
from math import *

x = array(eval(input()))
m = sum(x)/size(x)
a=0

for i in range(size(x)):
	a = a + (x[i]-m)**2
	b = (size(x)-1)
d = sqrt(a/b)
	
	
print(round(d, 3))
