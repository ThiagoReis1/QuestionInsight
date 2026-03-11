x = input("medida")
y = int(input("valor da medida"))
P = 0,393701 * y
C = y / 0,393701
if (x == 'P'):
	print(round(C))
if (x == 'C'):
	print(round(P, 2))

