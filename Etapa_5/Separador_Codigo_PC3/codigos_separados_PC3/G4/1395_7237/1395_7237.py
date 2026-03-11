v = float(input("valor de vendas:"))
if v>= 1000:
	a = (5/100)*v
else:
	a = (15/100)
print(round(a, 2))