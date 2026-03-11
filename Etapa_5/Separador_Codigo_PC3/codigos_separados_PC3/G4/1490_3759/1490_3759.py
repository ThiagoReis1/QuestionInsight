ca=float(input("Digite aqui o consumo:"))

if(ca >= 0):
	if(ca > 0.0 and ca <10.0 ):
		t = 3.00
		ta = 15.00
		v = ca *t + ta
		print(round(v,2))
	elif(ca > 10.0 and ca < 15.0 ):
		t = 3.50
		ta = 20.00
		v = ca *t + ta
		print(round(v,2))
	elif(ca > 15.0 and ca < 20.0 ):
		t = 4.00
		ta = 25.00
		v = ca * t + ta
		print(round(v,2))
	else:
		t = 4.50
		ta = 30.00
		v = ca *t + ta
		print(round(v,2))
