molecula = input("nome da molecula:").lower()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if(molecula == "histidina"):
	histidina = (C*5) + (H*8) + N + (O*4)
	print(round(histidina, 2))
elif(molecula == "glutamina"):
   glutamina = (C*5) + (H*8) + N + (O*4)
	print(round(glutamina, 2))
elif(molecula == "prolina"):
	prolina = (c*5) + (H*10) + N + (o*2) 
	print(round(prolina, 2))
else:
	print("Entrada:", molecula)
   print("Dado invalido")


