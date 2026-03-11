Pesq = input("Pesquisa (SIM/NAO) ")


i = 0


while (Pesq != "S"):
	while (Pesq == "SIM" or Pesq == "NAO"):
		if(Pesq == "SIM"):
			i = i + 1
		else:
			i = 0
			
		Pesq = input("Pesquisa (SIM/NAO) ")

print (i)