from numpy import*
v = array(eval(input("Informe os valores da compra: \n")))
i = 0
soma = 0							
while(i<size(v)):
	if(v[i]>80):
		soma = soma + 1
	i = i + 1
desconto = soma*5
vetor = sum(v)
total = vetor - desconto
print(round(total,2))
