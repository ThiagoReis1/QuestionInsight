Ca = float(input("consumo de agua: "))

if (Ca >= 0.0) and (Ca <= 10.0):
	V = Ca * 3 + 15
	print(round(V, 2))
	
elif (Ca >= 10.0) and (Ca <= 15.0):
	V = Ca * 3.50 + 20
	print(round(V, 2))
	
elif (Ca >= 15.0) and (Ca <=20.0):
	V = Ca * 4 + 25
	print(round(V, 2))
	
elif (Ca >= 20.0):
	V = Ca * 4.50 + 30
	print(round(V, 2))
	