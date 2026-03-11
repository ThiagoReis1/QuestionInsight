x = float(input())
fx = 0

if -100 <= x and x < 0:
	fx = -1 * (1.0/x)
	print(round(fx, 4))
elif 0 < x and x <= 100:
	fx = 1.0 / x
	print(round(fx, 4))
else:
	print('entrada invalida')