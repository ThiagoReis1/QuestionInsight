lp = input("l/p: ").upper()
qtde = int(input("qtde de l ou p: "))
refri = int(input("qtde de refri: "))

pf = 6*qtde + refri*3
pf2 = 13.5*qtde + refri*3

if (lp == "P"):
	print(round(pf2,2))
else:
	print(round(pf,2))

