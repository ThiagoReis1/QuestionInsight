votos_AR = int(input("Digite aqui o numero de votos para Ambrosio:"))
votos_DO = int(input("Digite aqui o numero de votos para Delmeza :"))
total = votos_AR + votos_DO

if (votos_AR > votos_DO ):
	votos = (votos_AR * 100)/ total
	print("Ambrosio Rutra")
	print (round(votos,2))
else:
	votos = (votos_DO * 100)/ total
	print("Demelza Olecram")
	print (round(votos,2))