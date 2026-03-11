un = input("QUAL A UNIDADE DE MEDIDA(O/K)? ")
vl = float(input("VALOR A MEDIDA? "))

if(un.upper() == "K"):
	md = 35.274*vl
else:
	md = vl/35.274
	
print(round(md, 2))