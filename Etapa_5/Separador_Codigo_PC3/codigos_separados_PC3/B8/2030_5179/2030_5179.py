moeda = str(input("Insira o resultado [CARA ou COROA]: ")).upper()

i = 0
while (moeda != "S"):
	
	if (moeda == "COROA"):
		moeda = str(input("Insira o resultado novamente: ")).upper()
	
	elif (moeda == "CARA"):
		i = i + 1
		moeda = str(input("Insira o resultado novamente: ")).upper()
		
print(i)		
  