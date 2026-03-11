c  = float(input("consumo de minutos: "))
if(c <= 100):
	g = c * 1.20
else:
	g = 25 + 1.4 * c
print(round(g,2))