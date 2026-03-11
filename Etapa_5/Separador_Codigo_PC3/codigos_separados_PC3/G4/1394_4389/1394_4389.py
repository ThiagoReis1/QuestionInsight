h = float(input("Informe o numero de horas trabalhadas:\n"))
if (h <= 20):
	print(round(h*50,2))
else:
	x = h - 20
	print(round((50*20)+70*x,2))