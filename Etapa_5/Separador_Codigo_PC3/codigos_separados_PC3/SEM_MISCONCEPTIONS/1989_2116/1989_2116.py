amin = input("informe o aminoacido")
asparagina = 12.011*4 + 1.00794*8 + 14.00674*2 + 15.999*3
glutamina = 12.011*5 + 1.00794*8 + 14.00674 + 15.999*4
triptofano = 12.011*11 + 1.00794*11 + 14.00674*2 + 15.999*2

if(amin.upper() == "ASPARAGINA"):
	print(round(asparagina,2))
elif(amin.upper() == "GLUTAMINA"):
	print(round(glutamina,2))
elif(amin.upper() == "TRIPTOFANO"):
	print(round(triptofano,2))
else:
	print("Entrada" , amin.upper())
	print("Dado Invalido")

