pesquisa= input("Insira S para satisfeito, I para insatisfeito ou N para neutro: ")

contador= 0

while (pesquisa != "X"):
	if (pesquisa == "S"):
		contador= contador + 1 
	pesquisa= input("Insira S para satisfeito, I para insatisfeito ou N para neutro: ")
print(contador)