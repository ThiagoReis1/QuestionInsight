unidade = input("digite: ").upper()
ft = 0
i = 0

while unidade != "X":
	if unidade == "FT":
		ft = ft + 1
	unidade = input("digite: ")
	i = i + 1
print(ft)
