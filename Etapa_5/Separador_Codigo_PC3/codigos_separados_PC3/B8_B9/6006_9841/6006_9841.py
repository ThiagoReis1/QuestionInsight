batatas = int(input("Digite o numero de batatas: "))
if batatas < 10:
	preco = 0.90 * batatas
elif batatas >= 10:
	preco = 0.75 * batatas
print(round(preco, 2))