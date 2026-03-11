x = float(input("digite o valor de x: "))

if -100 <= x < 0:
	f= -1/x
	print(round(f, 4))
elif 0 < x <= 100:
	f= 1/x
	print(round(f, 4))
else:
	print("entrada invalida")