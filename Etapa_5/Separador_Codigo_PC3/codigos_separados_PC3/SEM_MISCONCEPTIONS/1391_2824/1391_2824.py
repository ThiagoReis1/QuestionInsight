conces = float(input("Qual o consumo de energia (em kWh)?"))

if(conces <= 150):
	val1 = (round(5 + conces*0.60, 2))
	print(val1)
else:
	val2 = (round(16 + conces*0.75, 2))
	print(val2)
