from numpy import *

v = array(eval(input("Vetor: ")))

va = 0
sz = size(v)

for i in range(1,sz):
	if (v[i] >= v[0]):
		va = va + 1

for i in range(1,sz):
	if (v[i] >= v[0]):
		print(i)
print(va)