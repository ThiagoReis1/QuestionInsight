
produtos = input("Quais sao os produtos? (C, E ou P): ").upper()

i = 0
cont = 0
quant = 0
quant1 = 0
quant2 = 0

while i < len(produtos):
	if produtos[i] == "C":
		cont = cont + 10.50
		quant = quant + 1
	if produtos[i] == "E":
		cont = cont + 8.75
		quant1 = quant1 + 1
	if produtos[i] == "P":
		cont = cont + 17.90
		quant2 = quant2 + 1
	i += 1
	
print(round(cont, 2), quant, quant1, quant2)
		
		