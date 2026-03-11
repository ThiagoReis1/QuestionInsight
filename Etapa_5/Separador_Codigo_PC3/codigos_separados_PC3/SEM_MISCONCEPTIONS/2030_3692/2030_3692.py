moeda = input()
qntcara = 0
while(moeda.upper() != "S" and moeda.upper() == "CARA" or moeda.upper() == "COROA"):
	if(moeda.upper() == "CARA"):
		qntcara = qntcara + 1
	moeda = input()
print(qntcara)		