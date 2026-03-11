from numpy import * 
vet = array(eval(input("Vetor de numeros: ")))

pont = 0

for i in range(size(vet)):
	if vet[i] == 1:
		pont+=10
	if vet [i] == 2:
		pont+=5
	if vet [i] == 3:
		pont+=0
	if vet[i] == 4:
		pont+=5
	if vet[i] == 5:
		pont+=20
	if vet[i] == 6:
		pont+=10
print(pont)		
		
		