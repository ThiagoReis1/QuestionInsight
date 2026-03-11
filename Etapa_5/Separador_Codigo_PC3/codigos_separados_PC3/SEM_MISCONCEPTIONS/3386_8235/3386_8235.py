unidade = input("medida: ")
angulo = float(input("valor: "))
Rad = 0.0174533*angulo
Gr = angulo/0.0174533
if (unidade=="R"):
	print(round(Gr,2))
if (unidade=="G"):
	print(round(Rad,2))