classificacao = int(input("Digite a classificacao da estrela: "))


if classificacao == 5:
	estrela = "brilhante"
	print(estrela)
	
elif classificacao < 5:
	estrela = "menor"
	print(estrela)
	
elif classificacao > 5:
	estrela = "maior"
	print(estrela)