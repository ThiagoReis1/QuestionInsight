from numpy import *

v = array(eval(input()))
cont1 = 0


for i in range(size(v)):
	if (v[i]%3 == 0):
		cont1 = cont1 + 1

v1 = zeros(cont1, dtype = int)
cont = 0

for e in range(size(v)):
	if (v[e]%3 == 0):
		
		v1[cont] = e
		cont = cont +1
		
print(cont1)
print(v1)