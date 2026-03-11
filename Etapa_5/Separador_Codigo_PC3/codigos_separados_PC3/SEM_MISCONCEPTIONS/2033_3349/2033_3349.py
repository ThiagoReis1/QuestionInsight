unidade = input("Insira a unidade academica: ").upper()
nICOMP = 0
while(unidade != "S"):
	if(unidade == "ICOMP"):
		nICOMP = nICOMP + 1
	unidade = input("Insira a unidade academica: ")

print(nICOMP)