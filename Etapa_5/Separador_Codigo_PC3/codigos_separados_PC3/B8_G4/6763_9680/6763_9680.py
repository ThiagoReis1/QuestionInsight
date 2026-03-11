tp = float(input("tempo: "))

fx = 5.00

if tp < 2:
	tt = fx + 1.25
	print(round(tt, 2))
elif tp == 2:
	tt = fx + 2.25
	print(round(tt, 2))
elif tp > 2:
	tt = fx + 3.25
	print(round(tt, 2))