result = input("Resultado: ")

preta = 0
vermelha = 0

while(result.upper() != "S"):
	if(result.upper() == "PRETA"):
		preta = preta + 1
	
	result = input("Resultado: ")

print(preta)