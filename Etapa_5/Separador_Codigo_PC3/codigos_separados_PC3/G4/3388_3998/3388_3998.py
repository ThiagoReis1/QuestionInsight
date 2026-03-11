y = input("(B/W): ").upper()
m = float(input("valor da medida: "))
B = 3.41214 * m
W = m / 3.41214
if(y == 'W'):
	print(round(B,2))
else:
	print(round(W,2))