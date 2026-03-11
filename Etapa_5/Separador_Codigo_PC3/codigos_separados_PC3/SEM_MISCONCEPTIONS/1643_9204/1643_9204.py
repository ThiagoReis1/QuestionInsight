from numpy import*
vet = array(eval(input("digite o vetor de notas:")))


for i in range(size(vet)):
	if vet[i] >= 5.0:
		print(i)
		
		
cont = zeros()
for i in range(size(vet)):
	if vet[i] >= 5.0:
	print(vet)