limite=float(input("valor do limite: "))
c1=float(input("compra 1: "))
c2=float(input("compra 2: "))
c3=float(input("compra 3: "))
c4=float(input("compra 4: "))


vt= (c1+c2+c3+c4)
print(round(vt,2))

if (vt<=limite):
	print("Dentro do limite")
else:
	print("Estourou o limite")