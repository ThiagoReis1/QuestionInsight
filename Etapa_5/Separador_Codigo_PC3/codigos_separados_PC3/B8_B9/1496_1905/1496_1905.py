tempo = float(input("Tempo de voo:"))
if (tempo>=0):
	if (tempo<=100):
		custo = tempo*80 + 3000
		print(round(custo,2))
	elif (tempo>100) and (tempo<=200):
		custo = tempo*90 + 4000
		print(round(custo,2))
	elif (tempo>200) and (tempo<=300):
		custo = tempo*100 + 5000
		print(round(custo,2))
	elif (tempo>300):
		custo = tempo*110 + 6000
		print(round(custo,2))