from numpy import*

vet = array(eval(input("Custo dos itens: ")))

i = 0
cont = 0

while(i < size(vet)):
	if(vet[i] > 90.0):
		cont = cont - 6.50
	soma = sum(vet) + cont
	i = i + 1
print(round(soma,2))