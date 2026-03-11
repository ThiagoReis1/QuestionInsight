x = float(input("quantidade: "))
if (x < 17.5 ):
	z = x + 1.5
elif (x >= 17.5) and (x < 35.0):
	z = x + 2.3
elif (x >= 35.0) and (x < 50.0):
	z =  x + 3.3
elif (x >= 50.0):
	z = x + 4.7

print(round(z, 2))
	
