from numpy import*
vet = array(eval(input("meta de vacinacao: ")))

n= size(vet)
x= 0
for i in range(n):
	if (vet[i] >= vet[0]):
		x = x + 1
	if (vet[i] >= vet[0] and i!= 0):
		print(i)

print(x-1)