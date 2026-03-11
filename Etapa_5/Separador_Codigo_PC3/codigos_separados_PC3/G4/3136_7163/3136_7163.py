from numpy import*
from math import*

v = array(eval(input("insira: ")))
s = 0
for i in range(size(v)):
	s = s + log(v[i] + 1)
					
m = exp(s/size(v)) - 1

print(round(m,2))