comida = input("Lanche ou Salgado? L/S: ")
quantidade_comida = int(input("Quantos? "))
bebida = int(input("Quantos refrigerantes? "))

Lanche = 5.00
Salgado = 3.50
Refrigerante = 4.00

if (comida == "L"):
	total = (Lanche * quantidade_comida) + (Refrigerante * bebida)
	print(total)
else:
	total = (Salgado * quantidade_comida) + (Refrigerante * bebida)
	print(total)
	
	