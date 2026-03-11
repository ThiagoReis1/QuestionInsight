respostas = input("sim ou nao: ").upper()
cont = 0
while(respostas != "S"):
	if(respostas == "SIM"):
		cont += 1
	respostas = input("sim ou nao: ").upper()
print(cont)