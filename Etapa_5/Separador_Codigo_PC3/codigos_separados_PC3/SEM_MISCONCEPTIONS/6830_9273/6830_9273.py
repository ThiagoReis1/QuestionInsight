from numpy import*

produto = input(":").upper()
compras = 0
i = 0

while i < len(produto):
	if produto[i] == "H": 
		compras = compras + 3.85
	if produto[i] == "L":
		compras = compras + 2.95
	if produto[i] == "E":
		compras = compras + 7.90
	i = i + 1
	
print(round(compras, 2))