lp = input("L / P: ")
q = int(input("insira a qtde: "))
r = int(input("insira a qtde de refrigerante: "))

if (lp.upper() == "P"):
	total = q * 4.50 + r * 3.00
	print(round(total, 2))
	
else:
	total = q * 6.00 + r * 3.00
	print(round(total, 2))