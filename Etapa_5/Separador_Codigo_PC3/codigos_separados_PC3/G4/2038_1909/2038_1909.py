from math import*
A = input("atend satisfatorio: ")
soma = 0

while(A.upper() != 'S'):
	if(A.upper() == 'SIM'):
		soma = soma + 1

	A = input("atend satisfatorio: ")
print(soma)