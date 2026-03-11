a = int(input())
p1 = 50 * a
p2 = (50 * a) + ( 70 * (a - 20))
if (a <= 20):
	print(round(p1, 2))
else:
	print(round(p2, 2))
