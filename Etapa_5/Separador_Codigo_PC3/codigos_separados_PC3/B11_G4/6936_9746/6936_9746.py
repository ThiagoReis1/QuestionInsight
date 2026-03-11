x = float(input())
f = input()

if f == ("D"):
	z = x *  0.87
	print(round(z, 2))
if f == ("P"):
	z = x * 0.87
	print(round(z, 2))
if f == ("C"):
	y = float(input())
	if y == 1:
		print(round(x, 2))
	else:
		z = x + x * 0.08
		print(round(z, 2))