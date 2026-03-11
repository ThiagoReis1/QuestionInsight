tempo_p = float(input("tempo de permanencia: "))

if tempo_p < 2:
	vt = 5 + 1.25
	print(round(vt,2))
	
elif tempo_p == 2:
	vt = 5 + 2.25
	print(round(vt,2))
	
elif tempo_p > 2:
	vt = 5 + 3.25
	print(round(vt,2))