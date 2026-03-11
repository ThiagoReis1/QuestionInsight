h = float(input("horas"))
f = float(input("faltas"))

l = h - 2/3 * f

if (l >600):
	G = 300.0
	print(h,"extras e",round(f,2),"de falta")
	print("R$", G)
	
if (l <= 600):
	G =200.0
	print(h,"extras e",round(f,2),"de falta")
	print("R$", G)