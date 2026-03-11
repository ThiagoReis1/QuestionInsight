pesquisa = input("digite se S ou N: ")
soma = 0 
while pesquisa != "S":
	if pesquisa == "SIM":
		soma  += 1
	pesquisa = input("digite se S ou N: ")
print(soma)