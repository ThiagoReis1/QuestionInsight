x  = float(input())

if -4 <= x and x < 0:
	fx = (abs(x))**0.5
	print(round(fx, 4))
elif 0<= x and x<=4:
	fx = x**0.5
	print(round(fx, 4))
else:
	print("entrada invalida")