w = input("T ou S:").upper()
q = int(input("Quantidade:"))
a = int(input("Quantidade de acai:"))
if (w == "T"):
	o = q*3.50 + a*13.00
	print(o)

else:
	m = q*5.00 + a*13.00
	print(m)