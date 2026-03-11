ph = int(input("horas trabalhadas: "))

hora1 = ph * 50
hor = ph - 20
vs = hor * 70
hora2 = 1000 + vs

if (ph <= 20) :
	print(round(hora1, 2))
else :
	print(round(hora2, 2))