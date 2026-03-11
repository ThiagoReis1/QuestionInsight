

cons = float(input("consumo de internet: "))

if cons <= 100:
	saida = cons * 1.20
	
else:
	saida = (cons * 1.40) + 25
	
print(round(saida, 2))
