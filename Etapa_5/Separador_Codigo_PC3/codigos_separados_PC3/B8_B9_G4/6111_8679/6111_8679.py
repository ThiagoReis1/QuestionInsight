c = float(input())

if c < 17.5:
	v = c + 10.5
	print(round(v, 1))
elif c >= 17.5 and c < 35.:
	v = c + 14.
	print(round(v, 1))
elif c >= 35. and c < 50.:
	v = c + 18.6
	print(round(v, 1))
elif c >= 50.:
	v = c + 24.5
	print(round(v, 1))