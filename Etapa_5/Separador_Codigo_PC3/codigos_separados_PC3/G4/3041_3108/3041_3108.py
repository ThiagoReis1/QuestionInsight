x = float(input())

if((-1000 <= x) and (x < -2)):
	fx = -1 / (x+2)
	print(round(fx, 4))
elif((2 < x) and (x <= 1000)):
	fx = 1 / (x-2)
	print(round(fx, 4))
else:
	print("entrada invalida")