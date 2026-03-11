x=float(input())
fx=-1/x
fx2=1/x
if(x >= -100) and (x < 0):
	print(round(fx, 4))
else:
	if(x > 0) and (x <= 100):
		print(round(fx2, 4))
	else:
		print("entrada invalida")