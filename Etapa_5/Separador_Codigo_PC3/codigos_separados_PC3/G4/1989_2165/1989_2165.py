nome = input()

if(nome.upper() == "ASPARAGINA"):
	peso = 12.011*4 +  1.00794*8 + 14.00674*2 + 15.999*3
	print(round(peso, 2))
elif(nome.upper() == "GLUTAMINA"):
	peso = 12.011*5 + 1.00794*8 + 14.00674*1 + 15.999*4
	print(round(peso, 2))
elif(nome.upper() == "TRIPTOFANO"):
	peso = 12.011*11 + 1.00794*11 + 14.00674*2 + 15.999*2
	print(round(peso, 2))
else:
	print("Entrada: ",nome)
	print("Dado Invalido")
	