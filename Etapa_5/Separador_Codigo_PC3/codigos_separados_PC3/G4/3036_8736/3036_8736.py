x = float(input("Valor de x : "))

if (x <= -1) or (x >= 1):
	print(x)
elif (-1 < x < 0) or (0 < x < 1):
	print(1)
elif (x == 0):
	print(2)
else :
	print("SLA")