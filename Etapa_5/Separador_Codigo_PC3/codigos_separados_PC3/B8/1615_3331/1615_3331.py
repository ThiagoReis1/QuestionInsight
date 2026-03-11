from numpy import *

vetor= array(eval(input("Digite: ")))
vet=  array(eval(input("Digite vet: ")))

cont= 0
cont2= 0

soma= 0
soma2= 0

while(cont < size(vetor)):
	if vetor[cont] == 1:
		soma= soma + 40
	elif vetor[cont] == 2:
		soma= soma + 20
	elif vetor[cont] == 3:
		soma= soma + 10
	elif vetor[cont] == 4:
		soma= soma + 0
	cont=cont + 1
	
while(cont2 < size(vet)):
	if vet[cont2] == 1:
		soma2= soma2 + 40
	elif vet[cont2] == 2:
		soma2= soma2 + 20
	elif vet[cont2] == 3:
		soma2= soma2 + 10
	elif vet[cont2] == 4:
		soma2= soma2 + 0
	cont2= cont2 + 1
	
if soma > soma2:
	print("JOGADOR UM")
elif soma < soma2:
	print("JOGADOR DOIS")
	
#else:
#saida= 0
#cont= cont + 1
	

	
