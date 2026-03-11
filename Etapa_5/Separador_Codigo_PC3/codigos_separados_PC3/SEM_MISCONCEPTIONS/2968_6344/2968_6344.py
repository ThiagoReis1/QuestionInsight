escolha = input("Digite o que voce deseja: ")
numlanches = int(input("Digite a quantidade de lanches ou salgados: "))
numrefri = int(input("Digite a quantidade de refrigerantes: "))



if (escolha == 'L'):
	pagar = 5.0 * numlanches
	total = pagar + (numrefri * 4.0)
else:
		pagar = 3.50 * numlanches
		total = pagar + (numrefri * 4.0)
print(total)
	
	

