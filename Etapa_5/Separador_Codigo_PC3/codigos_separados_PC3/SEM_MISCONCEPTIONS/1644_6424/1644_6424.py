from numpy import *
a = array(eval(input()))
rep = 0
indice = -1
for c in range(size(a)):
	if a[c] < 5:
		rep += 1
print(rep)
v = []
for i in range(size(a)):
		indice += 1
		if a[i] < 5:
			v.append(indice)
vetor = array(v)
print(vetor)