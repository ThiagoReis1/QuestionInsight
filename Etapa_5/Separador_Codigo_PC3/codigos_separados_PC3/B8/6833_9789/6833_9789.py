compras = input("")

i = 0 
valor = 0 

while i < len(compras):
	if compras[i] == "M":
		valor += 7.25
	elif compras[i] == "P":
		valor += 4.75
	elif compras[i] == "R":
		valor += 3.50
	i += 1 	
	
print(round(valor, 2))