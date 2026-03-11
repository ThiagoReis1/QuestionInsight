x = float(input())

if (x <= -1) or (x >= 1):
	valor = abs(x) ** (1/2)
	print(round(valor, 2))
	
elif (-1 < x < 0) or ( 0 < x < 1):
	valor = abs(x)
	print(round(valor, 2))

elif x == 0:
	print(x)