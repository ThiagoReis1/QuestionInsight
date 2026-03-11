from numpy import *
vetor_de_numeros = eval(input("Vetor de numeros: "))

i = 0

for anel in vetor_de_numeros:
	if anel == 1:
		i += 100
	elif anel == 2:
		i += 60
	elif anel == 3:
		i += 20
	elif anel == 4:
		i += 0

print(i)