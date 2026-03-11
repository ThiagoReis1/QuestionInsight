km = float(input())
chakra = float(input())
mts = km * 1000
chakraGasto = (mts / 10 * 30)

if chakra >= chakraGasto:
	print(chakraGasto)
	print("vai conseguir")
	
else:
	print(chakraGasto)
	print("nao vai conseguir")
	

