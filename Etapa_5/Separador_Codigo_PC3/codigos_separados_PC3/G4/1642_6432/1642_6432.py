from numpy import *

x = array(eval(input("")))

cont = 0

for i in range(size(x)):
	if (x[i]%5) == 0:
		cont += 1

vt = zeros(cont, dtype=int)
j = 0
for i in range(size(x)):
	if (x[i]%5) == 0:
		vt[j] = i
		j += 1

print(cont)
print(vt)