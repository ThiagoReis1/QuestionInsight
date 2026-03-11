from numpy import*

vet = array(eval(input("Digite o vetor: ")))

cont = 0
for i in range(size(vet)):
	if vet[i]%2==0:
		cont = cont + 1
		
print(cont)

z = zeros(cont,dtype=int)
j = 0
for i in range(size(vet)):
	if vet[i]%2==0:
		z[j] = i
		j = j + 1
print(z)