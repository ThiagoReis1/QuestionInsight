pesquisa = input("S ou I ou N: ")
soma_S = 0
while pesquisa != "X":
	if pesquisa == "S":
		soma_S += 1
	pesquisa = input("S ou I ou N:")
print(soma_S)