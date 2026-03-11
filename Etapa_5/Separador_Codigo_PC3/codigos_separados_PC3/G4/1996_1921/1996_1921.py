nome = input("nome do aminoacido: ").lower()
if(nome == "aspartato"):
	pa = (4*12.011) + (6*1.0079) + 14.0067 + (4*15.9994)
	print(round(pa,2))
elif(nome == "fenilalanina"):
	pf = (9*12.011) + (11*1.0079) + (2*15.9994) + 32.066
	print(round(pf,2))
elif(nome == "tirosina"):
	pt = (9*12.011) + (11*1.0079) + 14.0067 + (3*15.9994)
	print(round(pt,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")