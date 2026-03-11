unidade = input("insira uma qtdd: ").upper()
cont = 0
while unidade != "X":
	if unidade == "FT":
		cont += 1
	unidade = input("entre com: ").upper()
print(cont)