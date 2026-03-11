produto = input("insira: ").upper()

i = 0
soma = 0
cont = 0
cont1 = 0
cont2 = 0

while i < len(produto):
	if produto[i] == "A":
		soma = soma + 19.90
		cont += 1
	elif produto[i] == "L":
		soma = soma + 3.50
		cont1 += 1
	elif produto[i] == "P":
		soma = soma + 4.25
		cont2 += 1
	i += 1
	
print(round(soma, 2), cont, cont1, cont2)