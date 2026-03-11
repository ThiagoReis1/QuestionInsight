casa = input(" cor da casa ")
casas = 0
casas_1 = 0
while(casa.upper() != "S"):
	casas = casas + 1
	if(casa.upper() == "PRETA"):
		casas_1 = casas_1 + 1
		casa = input(" cor da casa ")
	elif(casa.upper() == "VERMELHA"):
		casa = input(" cor da casa ")
por = (casas_1/casas * 100)
print(casas)
print(round(por,2))
