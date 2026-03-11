import math
x = float(input())

if -4 <= x < 0:
	print(round(math.sqrt(abs(x)), 4))
elif x == 0:
	print(0)
elif 0 < x <= 4:
	print(round(math.sqrt(x), 4))
elif x > 4:
	print("entrada invalida")