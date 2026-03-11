from numpy import *
vet = array(eval(input("Digite o valor: ")))
i = 0
qtd = 0
while (i < size(vet)):
	if (vet[i] < 8.95):
		qtd = qtd + 1
	i = i + 1
	
print("8.95")
print(qtd)