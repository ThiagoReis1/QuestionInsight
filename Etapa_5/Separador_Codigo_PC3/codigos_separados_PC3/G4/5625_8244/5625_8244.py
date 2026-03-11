tipo = input("tapioca ou salgado: ").upper()
q = int(input())
a = int(input())

if(tipo == "T"):
	tot = float(q*5.5 + a*10)
	print(round(tot,1))
	
else:
	tot = float(q*4 + a*10)
	print(round(tot, 1))