x = float(input('entre com um x: '))
fx = 0 

if (x <= 1):
	fx = fx + 1
	print(round(fx, 2))
elif (x > 1) and (x <= 2):
	fx = fx + 2
	print(round(fx, 2))
elif (x > 2) and (x <= 3):
	fx = x*x
	print(round(fx, 2))
elif (x > 3):
	fx = x*x*x
	print(round(fx, 2))
else: 
	print(round("", 2))