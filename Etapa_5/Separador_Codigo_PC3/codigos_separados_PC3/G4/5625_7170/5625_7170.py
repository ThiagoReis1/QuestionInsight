a = input("Tapioca (T) ou Salgado (S)?" )

if a == "T":
	b = int(input("Quantidade de Tapiocas?: "))
	c = int(input("Quantidade de Acais?: "))
	x = (b*5.5)+(c*10.0)
	print(round(x, 2))
	
else:
	d = int(input("Quantidade de Salgados?: "))
	c = int(input("Quantidade de Acais?: "))
	y = (d*4.00)+(c*10.00)
	print(round(y, 2))