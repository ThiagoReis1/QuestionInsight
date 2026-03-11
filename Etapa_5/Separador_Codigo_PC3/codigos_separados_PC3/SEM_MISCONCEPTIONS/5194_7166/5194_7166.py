classe = input("Nivel missao (A/B): ")

if(classe == "B"):
	ninja = "Chunin"
	valor = float(input("inserir valor da missao: "))
	pagamento = valor - (valor*15/100)
	print("Classe: ", ninja)
	print(round(pagamento, 2))
else:
	valor = float(input("inserir valor da missao: "))
	ninja = "jounin"
	pagamento = valor - (valor*22/100)
	print("classe: ", ninja)
	print(round(pagamento, 2))
