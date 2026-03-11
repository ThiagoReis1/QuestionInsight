from numpy import *
vet = array(eval(input()))

cont = 0

for i in range(size(vet)):
	cont = cont+1
	
v = zeros(cont, dtype=int)
j=0
for i in range(size(vet)):
	if(vet[i]==0):
		v[i] = 9**2
	else:
		v[i] = (vet[i]-1)**2
	
	
print(v)