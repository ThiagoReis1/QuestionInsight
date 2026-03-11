var1 = input("Resposta: ")

soma = 0


while(var1.upper() != "S"):
	if (var1.upper() == "SIM"):
		soma = soma + 1
	var1 = input("Resposta: ").upper()
	
print(soma)

