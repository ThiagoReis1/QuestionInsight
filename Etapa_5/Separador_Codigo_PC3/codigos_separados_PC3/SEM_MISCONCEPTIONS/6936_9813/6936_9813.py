pagamento = str(input("Coloque a forma de pagamento (D) dinheiro (P) pix (C)cartao: "))
valor = int(input())
if (pagamento == "D") and (pagamento == "P"):
	X = valor * 0.13
	total = valor - X
	print(round(total,2))
elif pagamento == "C":
	 vezes = int(input("Quantas vezes: "))
		if vezes == 2:
			N = valor 
			total = 
			print(round(total,2))
		if vezes == 1:
			print(round(valor,2))
	