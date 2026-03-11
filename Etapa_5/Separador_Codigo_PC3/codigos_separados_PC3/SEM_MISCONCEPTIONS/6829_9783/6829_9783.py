from numpy import*
kax = input(": ").upper()
indice = 0 
soma = 0
while indice < (len(kax)):
	if kax[indice] == "A":
		soma = soma + 19.90
		indice = indice + 1
	elif kax[indice] == "L":
		soma = soma + 3.50
		indice = indice + 1
	else:
		soma = soma + 4.25
		indice = indice + 1
print(round(soma, 2))