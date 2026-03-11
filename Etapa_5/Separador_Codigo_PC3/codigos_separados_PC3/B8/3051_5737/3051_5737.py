consumo = float(input("Consumo em kWh: "))

if(consumo > 0 and consumo < 150):
	v = consumo * 0.60 + 5
	print(round(v,2))
elif(consumo >= 150 and consumo < 250):
		v = consumo * 0.65 + 8
		print(round(v,2))
elif(consumo >= 250 and consumo < 350):
		v = consumo * 0.70 + 12
		print(round(v,2))
elif(consumo >= 350):
		v = consumo* 0.75 + 16
		print(round(v,2))