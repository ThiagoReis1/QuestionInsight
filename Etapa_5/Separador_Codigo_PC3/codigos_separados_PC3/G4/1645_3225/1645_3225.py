from numpy import*

vet = array(eval(input("Digite o vetor: ")))
v = 0
for i in vet:
	if (i >= 2000):
		v = v + 1

x = zeros(v, dtype = int)		

v = 0
for j in range(size(vet)):
	if (vet[j] >= 2000):
		x[v] = j
		v = v + 1

print(v)	
print(x)	

