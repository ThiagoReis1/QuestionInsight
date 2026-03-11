from numpy import *

qnt = array(eval(input("")))

h = 0
y = 0
s = 0

for i in range(size(qnt)):
	if(qnt[i] % 2 == 0):
		h = h + 1
print(h)
	
nv = zeros(h, dtype = int)
for j in range(size(qnt)):
	if(qnt[j] % 2 == 0):
		nv[s] = j
		s = s + 1
print(nv)
	