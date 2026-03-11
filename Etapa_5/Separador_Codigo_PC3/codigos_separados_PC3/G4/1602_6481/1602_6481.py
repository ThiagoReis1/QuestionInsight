from numpy import *

v = array(eval(input()), dtype = float)

i = 0

while (i < size(v) and v[i] != max(v)):
	i = i + 1
	
print(i)