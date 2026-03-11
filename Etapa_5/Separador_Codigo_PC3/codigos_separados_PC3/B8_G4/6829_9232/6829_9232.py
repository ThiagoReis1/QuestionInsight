prod = input('produtos: ')
aco = 0
lat = 0
pad = 0
i = 0
while(i < len(prod)):
	if(prod[i] == 'A'):
		aco += 1
	elif(prod[i] == 'L'):
		lat += 1
	elif(prod[i] == 'P'):
		pad += 1
	i += 1
aco1 = (aco * 19.90)
lat1 = (lat * 3.50)
pad1 = (pad * 4.25)
valor = (aco1 + lat1 + pad1)
print(round(valor, 2))