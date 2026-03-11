comida = (input("s ou b"))
q = float(input("quantidade"))
c = float(input("cappucino"))
if comida.upper() == "S":
	preco= (q* 4) +(c*7.5)
else:
	preco=(q * 5) + (c*7.5)
print(round(preco,2))