amino = input("Digite o aminoacido:")

if(amino.upper() != "ALANINA") and (amino.upper() != "VALINA") and (amino.upper() != "TIROSINA"):
	print("Entrada:",amino)
	print("Dado Invalido")
else:
	if(amino.upper() == "ALANINA"):
		print(round(3*12.011 + 7*1.00794 + 14.00674 + 2* 15.9994,2))
	
	if(amino.upper() == "VALINA"):
		print(round(5*12.011 + 11*1.00794 + 14.00674 + 2* 15.9994,2))
	
	if(amino.upper() == "TIROSINA"):
		print(round(9*12.011 + 11*1.00794 + 14.00674 + 3* 15.9994,2))