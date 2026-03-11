numero = int(input("Digite o numero: "))
conta = numero % 43
quoc = numero // 43
if conta == 0:
	print(quoc)
	print("sim")
	
else:
	print(conta)
	print("nao")