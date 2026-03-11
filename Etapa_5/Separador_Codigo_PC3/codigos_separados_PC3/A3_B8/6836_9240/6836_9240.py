insumos = input("insumos: ")
total = 0
bebidas = 0
congelados = 0
mercearia = 0

i = 0
while i < len(insumos):
	insumo = insumos[i]
	if insumo == 'B':
		bebidas +=1
		total += 6.80
	elif insumo == 'C':
		congelados +=1
		total += 11.75
	elif insumo == 'M':
		mercearia +=1
		total += 5.90
	i += 1
	
total = round(total ,2)
print(total)