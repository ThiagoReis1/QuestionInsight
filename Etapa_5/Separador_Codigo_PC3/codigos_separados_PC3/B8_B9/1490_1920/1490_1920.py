#volume gasto
volume = float(input("Volume(cm3):"))
if(volume<=10.0):
	tarifa = 3.0
	taxa = 15.0
elif(volume<=15.0 and volume >10.0):
	tarifa = 3.5
	taxa = 20.0	
elif(volume<=20.0 and volume >15.0):
	tarifa = 4.0
	taxa = 25.0
elif(volume>20):
	tarifa = 4.5
	taxa = 30.0	
valor = volume * tarifa + taxa
print(round(valor,2))