votos_rutra=int(input("Quantidade de votos para o candidato Ambrosio Rubra:"))
votos_olecram=int(input("Quantidade de votos para o candidato Demelza Olecram:"))
total = votos_rutra + votos_olecram
if votos_rutra > votos_olecram:
	print("Ambrosio Rutra")
	porcentagem = (votos_rutra * 100) / total
	print(round(float(porcentagem), 2))
elif votos_olecram > votos_rutra:
	print("Demelza Olecram")
	porcentagem = (votos_olecram * 100) / total
	print(round(float(porcentagem), 2))