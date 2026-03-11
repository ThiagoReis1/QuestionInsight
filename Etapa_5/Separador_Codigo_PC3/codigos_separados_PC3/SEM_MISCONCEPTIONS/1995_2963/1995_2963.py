aminoacido = input("Nome do aminoacido\n")
elif(aminoacido.lower() == "aspartato"):
		pesomolecular = (4*12.011 + 6*1.00794 + 14.0067 + 4*15.9994)
		print(round(pesomolecular,2))
	if(aminoacido.lower() == "cisteina"):
		pesomolecular = (3*12.011 + 7*1.00794 + 14.0067 + 2*15.9994 + 32.066)
		print(round(pesomolecular,2))
	if(aminoacido.lower() == "metionina"):
		pesomolecular = (5*12.011 + 11*1.00794 + 14.0067 + 2*15.9994 + 32.066)
		print(round(pesomolecular,2))
print("Entrada: x\nDado Invalido")