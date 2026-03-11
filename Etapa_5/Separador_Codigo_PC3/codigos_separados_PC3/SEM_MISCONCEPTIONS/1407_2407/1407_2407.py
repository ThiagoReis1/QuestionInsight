hp0 = float(input("HP inicial: "))


d1 = int(input("valor do dado 1: "))
d2 = int(input("valor do dado 2: "))
d3 = int(input("valor do dado 3: "))

vida_perdida = 10 * (d1+d2+d3)

vida_restante = hp0 - vida_perdida

if (vida_restante > 0):
	print(int(vida_restante))
	print("VIVO")
else:
	print(0)
	print("MORTO")
