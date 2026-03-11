prod = input('produtos: ').upper()
i = 0
mer = 0
pad = 0
rot = 0
while(i < len(prod)):
	if (prod[i] == 'M'):
		mer += 1
	elif(prod[i] == 'P'):
		pad += 1
	elif(prod[i] == 'R'):
		rot += 1
	i += 1
mer1 = (mer * 7.25)
pad1 = (pad * 4.75)
rot1 = (rot * 3.50)
valor = (mer1 + pad1 + rot1)
print(round(valor, 2))