opcao = input("Digite a opcao: ")
quantidade = int(input("Digite a quantidade: "))
quanticapu = int(input("Digite a quantidade de cappuccino: "))

if opcao.upper() == "B":
	total = 3.00 * quantidade + 5.50 * quanticapu
else:
	total = 6.00 * quantidade + 5.50 * quanticapu

print(round(total, 2))