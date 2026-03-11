unidade = input("Entre com ICE, FT ou ICOMP: ").upper()

ft = 0

while unidade != "X":
	if unidade == "FT":
		ft = ft + 1
	unidade = input("Entre com ICE, FT ou ICOMP: ").upper()

print(ft)