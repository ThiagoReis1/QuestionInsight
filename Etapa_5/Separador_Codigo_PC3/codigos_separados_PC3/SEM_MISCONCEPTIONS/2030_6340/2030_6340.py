moeda = input("Informe o resultado da moeda: ")
CARA = 0

while(moeda.upper() != "S"):
	if(moeda.upper() == "CARA"):
		CARA = CARA + 1
	moeda = input("Informe a proxima face: ")
print(CARA)	