from numpy import*
vet = array(eval(input("")))
i= 0
soma = 0
peso = 0
den = 0
while(i < size(vet)):
	peso = i + 1
	soma = soma + vet[i] * peso 
	den = den + peso
	i = i + 1
print(round(soma/den,2))