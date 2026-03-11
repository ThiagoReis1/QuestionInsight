aminoacido = input("Digite o nome do aminoacido: ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
if (aminoacido == "glicina".upper()):
	Pglicina = (C*2 + H*5 + N + O*2)
	print (float(round(Pglicina, 2)))
else:
	Pserina = (C*3 + H*7 + N + O*3)
	print (float(round(Pserina, 2)))
