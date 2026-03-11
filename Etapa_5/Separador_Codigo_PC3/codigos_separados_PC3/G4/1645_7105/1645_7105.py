from numpy import *

cont = 0
contx = 0

v = array(eval(input()))

for i in range(size(v)):
	if(v[i]>=2000):
		cont+=1
		
z = zeros(cont, dtype = int)

for j in range(size(v)):
	if(v[j]>=2000):
		z[contx] = j
		contx+=1

print(cont)
print(z)