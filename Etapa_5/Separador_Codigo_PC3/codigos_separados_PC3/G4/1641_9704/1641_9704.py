from numpy import *

vet= array(eval(input()))
t = 0
for i in range(0,size(vet)):
	if vet[i] % 3 == 0:
		t += 1
print(t)
aux = zeros(t,dtype=int)
a = 0
for i in range(0,size(vet)):
	if vet[i] % 3 == 0:
		aux[a] = i
		a += 1
print(aux)
		
