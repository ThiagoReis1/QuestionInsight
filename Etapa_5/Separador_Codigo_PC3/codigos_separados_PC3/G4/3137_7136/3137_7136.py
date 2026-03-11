from numpy import *

v = array(eval(input(": ")))
s = 0
i = 0

for i in range (size(v)):
	s = s + exp(v[i])
	
m = log(s/(exp(size(v))))

print(round(m, 2))