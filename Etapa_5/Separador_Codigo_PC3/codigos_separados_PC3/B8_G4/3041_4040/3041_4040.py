# Insertables

x = float(input("X coordinate: "))
f1 = -(1/(x + 2))
f2 = (1/(x - 2))

# Processing

if( (x >= -1000) and (x < -2) ):
	print(round(f1,4))
elif( (x > 2) and (x <= 1000) ):
	print(round(f2,4))
elif( (x < -1000) or ( (x > -2) and (x < 2) ) or (x > 1000) ):
	print("entrada invalida")