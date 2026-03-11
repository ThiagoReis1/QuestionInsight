p = float(input("leia o valor de vendas: "))
e1 = p * 0.05
e2 = (p * 0.05) + 200
if(p >= 1000.0):
	print(round(e1,2))
else:
	print(round(e2,2))