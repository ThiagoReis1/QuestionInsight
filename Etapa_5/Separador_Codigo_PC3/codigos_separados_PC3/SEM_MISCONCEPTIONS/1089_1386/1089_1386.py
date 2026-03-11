c1 = float(input("valor: "))
c2 = float(input("valor: "))
c3 = float(input("valor: "))
limite = float(input("valor do limite: "))
total = c1 + c2 + c3
print("%0.2f"%total)
if(total <= limite):
	print("sim")
else:
	print("Nao")