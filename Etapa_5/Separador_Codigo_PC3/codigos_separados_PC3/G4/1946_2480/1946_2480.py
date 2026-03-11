nome = input("Nome do aminoacido: ").lower()

if(nome == "fenilalanina"):
	peso = (12.011 * 9) + (11 * 1.0079) + (2 * 15.9994) + 32.066
	print(round(peso, 2))
else:
	peso = (12.011 * 9) + (11 * 1.0079) + 14.0067 + (3 * 15.9994)
	print(round(peso, 2))
	