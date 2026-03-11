consumo = int(input("digite o numero: "))

if(consumo != 0):
	if(consumo < 100):
		total = (0.50*consumo)+50
		print(round(total, 2))
	elif ((consumo >= 100) and (consumo < 250)):
	 	total = (0.75 * consumo) + 50.0
	 	print(round(total, 2))
	elif ((consumo >= 250) and (consumo < 500)):
	 	total = (1.00 * consumo) + 50.0
	 	print(round(total, 2))
	elif (consumo >= 500):
	 	total = (1.25 * consumo) + 50.0
	 	print(round(total, 2))

	


	