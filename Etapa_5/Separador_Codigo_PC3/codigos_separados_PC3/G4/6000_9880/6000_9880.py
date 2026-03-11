# Inserindo valores de entrada
c = int(input("Qual o numero de cachos de banana comprados?: "))

# Aplicando a condicional simples

if c < 3:
	c = 5.00 * c
	print(round(c , 2))

else:
	c = 4.25 * c
	print(round(c , 2))