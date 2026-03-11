c = input("Bolo ou croissant?: ")
q = float(input("Quantidade: "))
qc = float(input("Quantidade de cappuccinos: "))
if (c.upper() == "B"):
	c = 3
else:
	c = 6
v= c*q + qc*5.5
print(round(v,2))