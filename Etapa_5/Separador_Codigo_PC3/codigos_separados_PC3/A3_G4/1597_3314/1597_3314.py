from numpy import *
vet = array(eval(input("Digite o valor: ")))
i = 0
soma = 0
desconto = 5.00
while (i < size(vet)):
	if (vet[i] > 80.00):
		 desconto = vet[i] - 5
	else:	
		desconto = vet[i]
	soma = soma + desconto
	i = i + 1
print(round(soma,2))