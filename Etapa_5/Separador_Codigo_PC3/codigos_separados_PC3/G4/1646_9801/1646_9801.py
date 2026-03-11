from numpy import *

v = array(eval(input("Vetor? ")))
lim = 50
cont = 0

for e in range(size(v)):
	if v[e] <= lim:
		cont += 1
j = 0
v0 = zeros(cont, dtype = int)
for e in range(size(v)):
	if v[e] <= lim:
		v0[j] = e
		j = j + 1
print(cont)
print(v0)
#for e in range(size(v0)):
#	v0[e] = v0[e] + e
#print(v0)