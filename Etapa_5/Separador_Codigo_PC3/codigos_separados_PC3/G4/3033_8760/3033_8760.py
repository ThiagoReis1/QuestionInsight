x = float(input(""))

if ( x < 0) and (x >= -100):
	f = -1/x
	print(round(f, 4))
	
elif (x > 0) and (x <= 100):
	f = 1/x
	print(round(f, 4))
	
else: 
	print("entrada invalida")