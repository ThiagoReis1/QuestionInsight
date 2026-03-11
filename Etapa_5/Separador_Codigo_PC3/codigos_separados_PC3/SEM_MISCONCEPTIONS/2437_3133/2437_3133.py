abertura = float(input("Digite o valor da abertura: "))
fechamento = float(input("Digite o valor do fechamento: "))

percentual_negativo = (fechamento - abertura)/abertura
	
print(round(percentual_negativo * 100, 2))	