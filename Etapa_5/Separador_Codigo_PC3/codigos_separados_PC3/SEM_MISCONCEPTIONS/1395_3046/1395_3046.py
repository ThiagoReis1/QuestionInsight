v = float(input("informe o valor de vendas: "))

cond1 = (5/100)*v
cond2 = (v - 1000)*(10/100) + (5/100)*1000

if(v <= 1000):
	print(round(cond1, 2))
else:
	print(round(cond2, 2))
	