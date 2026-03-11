amino = input("aminoacido:").upper()
ox = 15.9994
carb = 12.011
nit = 14.00674
hid = 1.00794
if( (amino!= "ALANINA") and (amino!="VALINA") and (amino!= "TIROSINA")):
	print("Entrada:",amino)
	print("Dado Invalido")
elif((amino=="ALANINA")):
	pesomol = carb*3 + hid*7 + 2*ox + nit
	print(round(pesomol,2))	
elif((amino=="VALINA")):
	pesomol = carb*5 + hid*11 + 2*ox + nit
	print(round(pesomol,2))
elif((amino=="TIROSINA")):
	pesomol = carb*9 + hid*11 + nit + ox*3
	print(round(pesomol,2))