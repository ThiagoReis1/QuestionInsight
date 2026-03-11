v1 = float(input("consumo: "))
if (v1 <=150):
	m = v1*0.60+5
	print(round(m, 2))
else:
	m = v1*0.75+16
	print(round(m, 2))