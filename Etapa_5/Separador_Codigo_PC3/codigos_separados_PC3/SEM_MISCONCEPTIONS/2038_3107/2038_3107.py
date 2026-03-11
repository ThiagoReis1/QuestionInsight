entrada = input()

acum = 0

while(entrada.upper() != "S"):
	if(entrada.upper() == "SIM"):
		acum = acum + 1
	entrada = input()
print(acum)
	
		