from numpy import *
recorde = 8.95
i = 0
qtd = 0
vet = array(eval(input("Digite o valor dos vetores(saltos): ")))
while (i < size(vet)):
	if (vet [i] > 8.95):
		qtd = qtd + 1
		i = i + 1
	else:
		i = i + 1
print (recorde)
print (qtd)
