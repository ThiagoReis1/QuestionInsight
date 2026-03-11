comb = int(input(""))

if ((comb > 0) and (comb < 17.5)):
	zylium = 0.8
	total = zylium + comb
	print(round(total, 1))
	
elif ((comb >= 17.5) and (comb < 35)):
	zylium = 1.3
	total = zylium + comb
	print(round(total, 1))
	
elif ((comb >= 35) and (comb < 50)):
	zylium = 2.1
	total = zylium + comb
	print(round(total, 1))
	
elif (comb >= 50):
	zylium = 3.0
	total = zylium + comb
	print(round(total, 1))