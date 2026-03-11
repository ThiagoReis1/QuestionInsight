bol = input()
i = 0
g = 0

while(bol.upper() != "S"):
	if(bol.upper() == "PRETA"):
		i = i + 1
		g = g + 1
	elif(bol.upper() == "VERMELHA"):
		g = g + 1
	else:
		g = g
	
	bol = input()
	
print(g)
porc = (i/g) * 100
print(round(porc, 2))