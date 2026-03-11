aminoacido = input("Digite o nome do aminoacido: ").upper()

g = float((12.011*2)+(1.0079*5)+(14.00674*1)+(15.9994*2))
s = float((12.011*3)+(1.0079*7)+(14.00674*1)+(15.9994*3))

if g < s:
	print(round(g, 2))
else:
	print(round(s, 2))
	