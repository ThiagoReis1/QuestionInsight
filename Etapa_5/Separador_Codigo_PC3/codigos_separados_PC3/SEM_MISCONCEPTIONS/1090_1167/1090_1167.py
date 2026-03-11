c1 = float(input("valor: "))
c2 = float(input("valor: "))
c3 = float(input("valor: "))
c4 = float(input("valor: "))
limite = float(input("valor do limite: "))
total = round((c1 + c2 + c3 + c4),2)
if(total <= limite):
	print(total)
	print("Sim")
else:
	print(total)
	print("Nao")
	