x = int(input("Valor do dado1: "))
y = int(input("Valor do dado2: "))
r = int(input("Numero de rodadas: "))

if (x <= 1) and (x >= 6),
	(y <= 1) and (x >= 6):
		print("Entrada invalida!")	
elif (x + y == 12):
	pt = (x + y + 1)
	print("CONSTRICAO")
	print(pt)
elif (x + y > 5):
	pt = (x + y + 1) * r
	print("POLEN")
	print(pt)
else:
	pt = x * y
	print("FRANQUEZA")
	print(pt)