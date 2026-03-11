x = float(input("valor de x: "))
msg = 0
if (x <= -1) or ( x >= 1):
	msg = x
elif (-1 < x < 0) or (0 < x < 1):
	msg = (1)
else:
	x = 0
	msg = (2)
print(round(msg, 2))