

compras = input()

tam = len(compras)
cont = 0
total = 0
congelados = 0
enlatados = 0
pescados = 0
while(cont < tam):
	if(compras[cont] == "C"):
		total += 10.50
		congelados += 1
	elif(compras[cont] == "E"):
		total += 8.75
		enlatados += 1
	elif(compras[cont] == "P"):
		total += 17.90
		pescados += 1
	cont += 1

print(round(total, 2), congelados, enlatados, pescados)