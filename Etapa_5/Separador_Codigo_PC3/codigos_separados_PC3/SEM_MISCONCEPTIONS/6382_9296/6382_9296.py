from numpy import*

vet = array(eval(input("Digite os numeros")))

for i in range(size(vet)):
	if(vet[i] == 9):
		sucessor = 0
	else:
		sucessor = vet[i] + 1
	vet[i] = sucessor**2
print(vet)
		