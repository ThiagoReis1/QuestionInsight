aminoacido = input("nome do aminoacido: ")

if (aminoacido == "GLUTAMINA"):
	C = 12.011 * 5
	H = 1.00794 * 8
	N = 14.0067 * 1
	O = 15.9994 * 4
	pm = C + H + N + O
	print(round(pm,2))
elif (aminoacido == "SERINA"):
	C = 12.011 * 3
	H = 1.00794 * 7
	N = 14.0067 * 1
	O = 15.9994 * 3
	pm = C + H + N + O
	print(round(pm,2))
elif (aminoacido == "TREONINA"):
	C = 12.011 * 4
	H = 1.00794 * 9
	N = 14.0067 * 1
	O = 15.9994 * 3
	pm = C + H + N + O
	print(round(pm,2))
else:
	print("Entrada: " , aminoacido)
	print("Dado Invalido")