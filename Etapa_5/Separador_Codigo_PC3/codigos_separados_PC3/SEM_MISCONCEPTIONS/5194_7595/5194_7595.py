classificacao = input("Classificacao da missao: ").lower()
valor_pago = float(input("Valor pago na missao: "))

if(classificacao == "a"):
	valor_imposto = valor_pago * (22/100)
	valor_repassado = valor_pago - valor_imposto
	print("Classe: Jounin")
	print(round(valor_repassado,2))
else:
	valor_imposto = valor_pago * (15/100)
	valor_repassado = valor_pago - valor_imposto
	print("Classe: Chunin")
	print(round(valor_repassado,2))