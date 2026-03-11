comida = input("Escreva se voce deseja L ou P: ")
q1 = int(input("Escreva a quantidade de lanche ou pizza: "))
q2 = int(input("Escreva a quantidade de refrigerante: "))

if comida == "P":
	total = (q1 * 4.50) + (q2 * 3.00)
else:
	total = (q1 * 6.00) + (q2 * 3.00)

print(round(total, 2))
