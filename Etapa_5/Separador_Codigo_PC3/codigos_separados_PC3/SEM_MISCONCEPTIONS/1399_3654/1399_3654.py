votos_1 = float(input())
votos_2 = float(input())

votos_validos = (votos_1 + votos_2) 

if(votos_1 > votos_2):
	nome = "Ambrosio Rutra"
	porc_votos = (votos_1/votos_validos) * 100
	print(nome)
	print(round(porc_votos,2))
else:
	nome = "Demelza Olecram"
	porc_votos = (votos_2/votos_validos) * 100
	print(nome)
	print(round(porc_votos,2))