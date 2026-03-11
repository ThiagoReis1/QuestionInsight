from numpy import*
custo = array(eval(input("vetor de custo dos itens: ")))
i=0
soma=0
soma2=0

while(i < size(custo)):
	if (custo[i] >= 80):
		soma = custo[i]*0.85 + soma
		i=i+1
	else:
		soma2=custo[i] + soma2
		i=i+1
final = soma+soma2
print(round(final,2))