from numpy import *

n = array(eval(input('Digite as notas: ')))



acum = 0
for i in range(size(n)):
	if n[i] >= 5.0:
		acum = acum + 1

v1 = zeros(acum, dtype=int)

j = 0
l = 0
for i in range(size(n)):
	if n[i] >= 5.0:
		v1[j] = i
		j = j +1	
print(acum)
print(v1)
