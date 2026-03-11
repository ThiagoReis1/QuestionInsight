gcomum = float(input("mi de litros de combustivel comum: "))

if gcomum > 0 and gcomum <= 17.5:
	print(round(gcomum + 10.5,1))
	
elif gcomum > 17.5 and gcomum <= 35:
	print(round(gcomum + 14,1))
	
elif gcomum > 35 and gcomum <= 50:
	print(round(gcomum + 18.6,1))
	
else:
	print(round(gcomum + 24.5,1))
	