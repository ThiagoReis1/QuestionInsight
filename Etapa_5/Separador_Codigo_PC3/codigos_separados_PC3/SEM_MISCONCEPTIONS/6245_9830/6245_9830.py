pesquisa = input("para satisfeito (s), para insatisfeito (i), para neutros (n): ").upper()
cont = 0

while pesquisa == "S":
		cont = cont + 1
		pesquisa = input("(S), (i), (n)")
		print(cont)