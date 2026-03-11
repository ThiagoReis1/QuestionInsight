HT = float (input("Quantas horas foram trabalhadas?"))
pag = 50 * HT
pag2 =(HT - 20) * 70 + (20 * 50)
if (HT <= 20):
	print(round(pag,2))
	
else:
	print (round(pag2,2))