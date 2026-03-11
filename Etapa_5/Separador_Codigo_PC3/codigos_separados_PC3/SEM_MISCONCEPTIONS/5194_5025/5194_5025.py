classificacao = input("Classificacao da missao: ")
valor = float(input("Valor pago pela missao: "))

if classificacao == "A":
	pagamento = valor - (valor * 0.22)
	print("Classe: Jounin")
	print(round(pagamento,2))
else :
	pagamento2 = valor - (valor * 0.15)
	print("Classe: Chunin")
	print(round(pagamento2,2))