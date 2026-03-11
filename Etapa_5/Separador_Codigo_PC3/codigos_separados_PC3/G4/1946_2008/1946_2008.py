amino = input("nome do aminoacido: ")


if (amino == "fenilalanina"):
	C1 = 9 * 12.011
	H1 = 11 * 1.0079
	O1 = 2 * 15.9994
	S1 = 32.066
	total = C1 + H1 + O1 + S1
	print(round(total,2))
	
else:
	C2 = 9 * 12.011
	H2 = 11 * 1.0079
	N2 = 14.0067
	O2 = 3 * 15.9994
	total = C2 + H2 + N2 + O2
	print(round(total,2))
	
