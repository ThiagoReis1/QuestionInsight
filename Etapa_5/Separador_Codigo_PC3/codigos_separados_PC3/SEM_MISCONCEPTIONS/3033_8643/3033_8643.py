x = float(input(":"))

if(-100 <= x <0):
	total = -1/x
	print(round(total,4))
elif(0 < x <= 100):
	total = 1/x
	print(round(total,4))
else:
	print("entrada invalida")