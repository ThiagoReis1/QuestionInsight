entrada = input("digite o tipo de entrada:")
quantidade = int(input("digite a quantidade:"))
valor = 25.90 * quantidade
if (entrada.upper()== "B"):
	valor_total = valor - (valor * 10/100)
	
else: 
	valor_total = valor
print(round(valor_total,2))



