x = float(input())

if (x <= -1 or x >= 1):
	fx = x
	print(round(fx, 2))
elif (x > -1 and x < 0) or (x > 0 and x < 1):
	fx = 1
	print(round(fx, 2))
elif (x == 0):
	fx = 2
	print(round(fx, 2))