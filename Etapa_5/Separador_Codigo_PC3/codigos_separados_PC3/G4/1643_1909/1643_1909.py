from numpy import*
vet = array(eval(input()))
cont = 0

for i in range(size(vet)):
	if(vet[i] >= 5):
		cont = cont + 1
v= zeros(cont, dtype = int)

s=0
for i in range(size(vet)):
	if (vet[i] >= 5):
		v[s] = i
		s = s + 1 
print(cont)
print(v)