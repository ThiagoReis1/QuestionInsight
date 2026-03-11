compra = float(input("Insira o Valor Total da Compra: "))
opcao = input("Insira uma opcao de pagamento: Dinheiro (D) , Pix (P) , Cartao (C)").upper()

if opcao == "D" or opcao == "P":
	x = compra * 0.87
elif opcao == "C":
	parcela = input("Escolha se quer parcelar em 1 ou 2 vezes: ")
	if parcela == "1":
		x = compra
	elif parcela == "2":
		x = compra * 1.08
	else:
		print("Insira uma Opcao Valida")
else:
	print("Insira uma Opcao Valida")
	
print(round(x, 2))