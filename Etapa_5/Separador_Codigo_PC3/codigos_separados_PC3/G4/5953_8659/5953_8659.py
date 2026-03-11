c = input("lanche 'L' ou prato executivo 'P': ")
q = int(input("quantidade: "))
r = int(input("quantidade de refrigerante: "))
refri = r * 3
if c.upper() == "P":
	pf = refri + (q * 13.50)
else:
	pf = 6 * q + refri
print(pf)