from numpy import*

vet = array(eval(input("vetor: ")))

cont = 0

for i in range(size(vet)):
	if(i != 0) and (vet[i] >= vet[0]):
		print(i)
		cont = cont + 1
print(cont)