from numpy import *
ap = array(eval(input("Digite: ")))
cont = 0
p = 100 * 70/100
for i in range(len(ap)):
	if ap[i] >= p:
		cont += 1
vi = zeros(cont, dtype = int)
j = 0
for i in range(len(ap)):
	if ap[i] >= p:
		vi[j] += i
		j += 1
print(cont)
print(vi)