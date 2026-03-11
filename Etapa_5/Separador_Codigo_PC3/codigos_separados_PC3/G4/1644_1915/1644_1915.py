from numpy import*
vet = array(eval(input("digite o vetor: ")))
rep = 0

for i in range(size(vet)):
	if(vet[i] < 5):
		rep = rep + 1
print(rep)		
v0 = zeros(rep, dtype = int)
k = 0
for i in range(size(vet)):
	if(vet[i] < 5):
		v0[k] = i
		k = k + 1
print(v0)	