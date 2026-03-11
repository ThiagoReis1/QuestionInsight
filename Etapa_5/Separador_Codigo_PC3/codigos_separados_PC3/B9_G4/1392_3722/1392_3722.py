c = float(input())
if c < 10:
	print(round(30 + 3*c, 2))
elif c >= 10:
	print(round(30 + c * 3.5, 2))
else:
	print(round(30, 2))