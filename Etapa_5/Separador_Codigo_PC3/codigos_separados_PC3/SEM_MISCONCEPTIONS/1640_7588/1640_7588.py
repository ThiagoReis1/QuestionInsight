from numpy import *

h = array(eval(input()))

tV = 0

for i in range(size(h)):
	if(h[i] % 2 != 0):
		tV += 1

vCont = zeros(tV, dtype = int)

p = vCont

contInput = 0
contOutput = 0

for k in range(size(h)):
	if(h[k] % 2 != 0):
		p[contOutput] += contInput
		contOutput += 1
	contInput += 1


print(tV)
print(p)