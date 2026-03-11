lim = float(input("limite do cartao:"))
v1 = float(input("compra 1:"))
v2 = float(input("compra 2:"))
v3 = float(input("compra 3:"))
v4 = float(input("compra 4:"))

v = v1 + v2 + v3 + v4

if (v <= lim):
	total = v
	print(round(total,2))
	print("Dentro do limite")
else:
	total = v
	print(round(total,2))
	print("Estourou o limite")