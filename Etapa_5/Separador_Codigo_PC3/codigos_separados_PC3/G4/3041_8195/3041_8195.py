var1 = float(input('numero: '))
if(var1>= -1000 and var1 < -2):
	cal = -1/(var1 +  2)
	print(round(cal,4))
else:
	if(var1>2 and var1 <= 100):
		cal1 = 1/(var1 - 2)
		print(round(cal1,4))
	else:
		print('entrada invalida')