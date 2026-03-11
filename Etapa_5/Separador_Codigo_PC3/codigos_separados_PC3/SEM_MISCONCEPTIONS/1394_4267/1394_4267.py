horas = int(input("Digite a quantidade de horas: "))
if (horas <= 20):
	horas = 50*horas
	print(round(horas,2))
else:
	horas = 50*20 + (horas-20)*70
	print(round(horas,2))