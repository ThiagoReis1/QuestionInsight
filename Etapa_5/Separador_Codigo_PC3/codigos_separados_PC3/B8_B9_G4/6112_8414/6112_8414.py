x = float(input(" quantidade de combustivel comum: "))

if x < 17.5:
	print(round(10.5 + x, 2))
	
elif x >= 17.5 and x<=34.9: 
	print(round(14.0 + x, 2))
	
elif x >= 35.0 and x <= 49.9:
	print(round(18.6 + x, 2))
	
elif x >= 50.0:
	print(round(24.5 + x, 2))