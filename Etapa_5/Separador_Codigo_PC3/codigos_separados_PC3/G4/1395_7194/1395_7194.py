v = float(input("volume de vendas: "))

if v <= 1000:
	p = (5/100)*v
else:
	p = (5/100)*1000 + (10/100)*v
print(round(p,2))