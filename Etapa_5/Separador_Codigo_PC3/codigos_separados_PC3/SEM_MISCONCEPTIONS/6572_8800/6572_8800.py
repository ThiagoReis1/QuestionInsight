numero = int(input("digite a quantidade de pizzas: "))

if numero < 3:
	taxa = 3
	valor = taxa + (5 * numero)
elif numero == 3:
	taxa = 3.25
	valor = taxa + (5 * numero)
else:
	taxa = 4.5
	valor = taxa + (5 * numero)
print("total=", valor)