valor = float(input("Qual o valor total da compra: "))
opcao = str(input("Qual a opcao de compra, [D] no dinheiro, [p] no pix e [C] no cartao: ")).upper()
if opcao == "C":
	vezes = int(input("Quantas vezes deseja pagar, 1 ou 2? "))
	if vezes == 1:
		total = valor
		print(round(total,2))
	elif vezes == 2:
		total = valor * 0.06 + valor
		print(round(total,2))
elif opcao == "P" or opcao == "D" :
	total = valor - valor * 0.11
	print(round(total,2))