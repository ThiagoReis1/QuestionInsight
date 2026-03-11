opcao = input("Opcao: "). upper()
i = 0
pagamento = 0.
while i < len(opcao):
	if opcao[i] == "D":
		pagamento += 2.25
	elif opcao[i] == 'S':
		pagamento += 4
	elif opcao[i] == 'I':
		pagamento += 6.9
	i += 1
print(round(pagamento , 2))