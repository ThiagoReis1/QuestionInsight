nome = input("nome do aminoácido:")
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
if (nome.upper() == "GLICINA"):
	peso = 2*c+h*5+n+o*2
	print(round(peso,2))
else:
	serina =(c*3+h*7+n+o*3)
	print(round(serina,2))
