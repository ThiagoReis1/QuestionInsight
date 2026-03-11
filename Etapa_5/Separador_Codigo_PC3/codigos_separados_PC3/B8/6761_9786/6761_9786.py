consumo = float(input())
fixo = 60
					 
if consumo < 50:
	total = 4.50 + fixo
					 
elif consumo == 50:
	total = 5.50 + fixo
					 
elif consumo > 50:
	total = 6.50 + fixo
						 					 
print(round(total,2))