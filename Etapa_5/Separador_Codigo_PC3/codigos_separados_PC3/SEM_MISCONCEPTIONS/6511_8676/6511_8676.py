entrada = input("entrada: ")
qntdd = float(input("Q "))
if entrada.upper() == "B":
	total = 25.9 * qntdd
	desconto = total * 0.1
	valor = total - desconto
	print(round(valor,2))
else:
	total = 25.9 * qntdd
	print(round(total,2))
