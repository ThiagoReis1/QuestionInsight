pesquisa = input("P ou I ou V: ").upper()
soma_P = 0
while pesquisa != "S":
	if pesquisa == "PRETA":
		soma_P += 1
	pesquisa = input("P ou I V: ").upper()
print(soma_P)
	
	