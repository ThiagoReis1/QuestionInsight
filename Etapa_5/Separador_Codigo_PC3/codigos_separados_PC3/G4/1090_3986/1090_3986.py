lc=float(input("limite do cartao: "))
v1=float(input("compra 1: "))
v2=float(input("compra 2: "))
v3=float(input("compra 3: "))
v4=float(input("compra 4: "))
v=round(v1 + v2 + v3 + v4,2)
if (v <= lc):
	print(v)
	print("Dentro do limite")
else :
	print(v)
	print("Estourou o limite ")