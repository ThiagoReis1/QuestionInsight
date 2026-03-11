from numpy import*

vet = array(eval(input("Digite o valor: ")))

cont = 0


for i in range(size(vet)):
	if vet[i] > 90:
		cont = cont + 6.50
	
print(round(sum(vet) - cont, 2))