nome = input("nome do aminoacido: ")



if (nome == "fenilalanina"):
	C1 = 12.011 * 9
	H1 = 1.0079 * 11
	O1 = 15.9994 * 2
	S1 = 32.066
	total = C1 + H1 + O1 + S1
	print(round(total,2))
	
else:
	C1 = 12.011 * 9
	H1 = 1.0079 * 11
	N1 = 14.0067 * 1 
	O1 = 15.9994 * 3
	total = C1 + H1 + N1 + O1
	print(round(total,2))