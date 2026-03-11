from numpy import *

v = array(eval(input(":")))
i = 0
x = 1/6
for i in range(size(v)):
	v[i]= v[i]**x
	i = i+1

n = sum(v)/size(v)
m = n**6
print(round(m,2))
