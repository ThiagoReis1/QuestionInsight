compra = float(input("Digite o valor total da compra: "))
pagamento = input("Digite D para dinheiro e p para pix ou C para credito: ").upper()

if pagamento == "D" or pagamento == "P":
	desconto = compra -(0.19 * compra)
	print(round(desconto,2))
elif pagamento == "C":
	parcelas = int(input("De quantas vezes sera o pagamento? "))
	if parcelas == 1:
		print(compra)
	else: 
		desconto = compra + (0.09 * compra)
		print(round(desconto,2))
	