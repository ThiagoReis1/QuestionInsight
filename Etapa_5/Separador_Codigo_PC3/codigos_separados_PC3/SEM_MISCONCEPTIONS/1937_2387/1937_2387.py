#Dois aminoacidos: Alanina e Valina

#leitura do aminoacido

amino = input("")
if(amino.upper() == "ALANINA"):
	x = ((3*12.011) + (7*1.00794) + (14.00674) + (2*15.9994))
	print(round(x,2))
if(amino.upper() == "VALINA"):	
	y = ((5*12.011) + (11*1.00794) + 14.00674 + (2*15.9994))
	print(round(y,2))