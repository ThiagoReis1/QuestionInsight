quant_votos1 = int(input("Digite a quantidade de votos: "))
quant_votos2 = int(input("Digite a quantidade de votos: "))

if (quant_votos1 > quant_votos2):
	cand = "Ambrosio Rutra"
	print (cand) 
	total = quant_votos1 / (quant_votos1 + quant_votos2) * 100
	print (round (total, 2))
	
else:
	cand = "Demelza Olecram"
	print  (cand)
	total = quant_votos2 / (quant_votos2 + quant_votos1) * 100
	print (round (total, 2))
	
	
