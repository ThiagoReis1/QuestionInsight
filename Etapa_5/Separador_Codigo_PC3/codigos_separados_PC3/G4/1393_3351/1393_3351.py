#Entradinhas
a = float(input("Insira a massa da carga: "))
#Calculando frete
if(a >= 5000.0):
	b = (0.04*a) + 60
	print(round(b,2))
else:
	c = 0.05*a
	print(round(c,2))