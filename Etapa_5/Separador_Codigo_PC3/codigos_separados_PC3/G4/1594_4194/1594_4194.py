from numpy import*

A = array(eval(input("Dano do ataque: ")))

i = 0
peso = 1
acum = 0

while( i < size(A)):
	acum = acum + ( A[i] * peso )
	
	i = i + 1
	peso = peso + 1
	
print(acum)