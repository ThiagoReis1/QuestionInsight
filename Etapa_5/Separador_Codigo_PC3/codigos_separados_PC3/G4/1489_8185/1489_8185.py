e = float(input("Energia (kWh): "))

if e >= 0 and e <=150:
	v = e*0.6 + 5
	print(round(v, 2))
elif e > 150 and e <=250:
	v = e*0.65 + 8
	print(round(v,2))
elif e > 250 and e <= 350:
	v = e*0.7 + 12
	print(round(v, 2))
else:
	v = e*0.75 + 16
	print(round(v, 2))
	

	