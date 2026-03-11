from numpy import *

v = array(eval(input("Vetor? ")))
i = 0

for e in v:
	v[i] = v[i] * 2
	i += 1
print(v)