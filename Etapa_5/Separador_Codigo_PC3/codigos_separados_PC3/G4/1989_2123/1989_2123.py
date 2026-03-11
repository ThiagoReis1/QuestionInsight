am = input("digite o nome do aminoacido:").upper()

if(am == "ASPARAGINA" ):
	pm = (12.011*4)+(1.00794*8)+(14.00674*2)+(15.999*3)
	print(round(pm,2))
elif(am == "GLUTAMINA" ):
	pm1 = (12.011*5)+(1.00794*8)+(14.00674*1)+(15.999*4)
	print(round(pm1,2))
elif(am == "TRIPTOFANO" ):
	pm2 = (12.011*11)+(1.00794*11)+(14.00674*2)+(15.999*2)
	print(round(pm2,2))
else:
	print("Entrada:", am )
	print("Dado Invalido")