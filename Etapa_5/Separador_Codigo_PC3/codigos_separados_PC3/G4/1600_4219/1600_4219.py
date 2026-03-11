from numpy import*
vet = array(eval(input("digite um vetor :")))
cont = 0 
tam = size(vet)
soma = 0 
soma2 = 0
while cont< tam :
	if vet[cont]>80 :
		des = vet[cont]*15/100
		valor = vet[cont] - des 
		soma = soma + valor
		
	else :
		num = vet[cont]
		soma2 = soma2 + num
		
	cont = cont + 1
tudo = soma + soma2
print(round(tudo, 2))
	
	