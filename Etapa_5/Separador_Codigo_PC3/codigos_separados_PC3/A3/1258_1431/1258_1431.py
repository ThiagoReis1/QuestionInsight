from numpy import *
numero = float(input("digite o valor:"))
vetorx = array(eval(input("insira o vetor:")))
vetory = array(eval(input("insira o outro vetor:")))
q = (numero/numero+1)
i = 0
soma = 0
while (i <= size(vetorx)):
	for i in range (size(vetorx)):
		valorx = array([vetorx[i] * numero])
	for i in range (size(vetory)):
		valory = array([vetory[i]*numero])
somavetor = valorx + valory
resultado0 = soma + abs(somavetor[i]) ** q
resultado1 = resultado0 ** (1/q)
resultado2 = round(resultado2,3)
print(resultado2)