from numpy import *

vetor = array(eval(input("Vetor : ")))
v = zeros(size(vetor),dtype = int)
i = 0

for x in vetor:
	x = x * 2
	v[i] = x
	i = i + 1
print(v)