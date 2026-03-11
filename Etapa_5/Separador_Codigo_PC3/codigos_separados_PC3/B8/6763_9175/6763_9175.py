tarifa = float(input("Digite o tempo: "))

tarifa_fixa = 5.00

if tarifa <2: 
	tarifa_total = tarifa_fixa + 1.25
	print(tarifa_total)
	
elif tarifa ==2:
	tarifa_total = tarifa_fixa + 2.25
	print(tarifa_total)
	
elif tarifa >2:
	tarifa_total = tarifa_fixa + 3.25
	print(tarifa_total)
	
	