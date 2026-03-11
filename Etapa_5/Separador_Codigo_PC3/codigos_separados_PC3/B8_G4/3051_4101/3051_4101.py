e = float(input("Consumo de energia: "))

if(0<=e<=150):
	v = e*0.60 + 5.00
	print(round(v, 2))
elif(150<e<=250):
	v = e*0.65 + 8.00
	print(round(v, 2))
elif(250<e<=350):
	v = e*0.70 + 12.00
elif(e>350):
	v = e*0.75 + 16.00
	print(round(v, 2))