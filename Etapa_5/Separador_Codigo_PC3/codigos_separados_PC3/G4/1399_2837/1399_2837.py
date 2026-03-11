qtd1 = int(input("informe a quantidade de votos do candidato Ambrosio Rutra: "))
qtd2 = int(input("informe a quantidade de votos da candidata Demelza Olecram: "))
mensagem1 = "Ambrosio Rutra"
mensagem2 = "Demelza Olecram"

qtd3 = qtd1 + qtd2


if (qtd1 > qtd2):
	x = (qtd1 / qtd3)  * 100 
	
	print(mensagem1)
	print(round(x,2))
	
else:
	x2 = (qtd2 / qtd3) * 100	
	print(mensagem2)
	print(round(x2,2))
	
	