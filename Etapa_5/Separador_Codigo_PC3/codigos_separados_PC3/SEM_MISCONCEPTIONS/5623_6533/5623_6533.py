escolha = input("Digite o que voce deseja: ").upper()
numlanches = int(input("Digite a quantidade de bolo ou salgados: "))
numcappu = int(input("Digite a quantidade de cappuccinos: "))

if (escolha == 'B'):
	pagar = 5.0 * numlanches
	total = pagar + (numcappu * 7.50)
else:
	pagar = 4.0 * numlanches
	total = pagar + (numcappu * 7.50)
print(round(total, 2))
	