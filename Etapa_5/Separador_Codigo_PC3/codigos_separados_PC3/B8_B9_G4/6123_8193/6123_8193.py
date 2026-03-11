c = float(input("combustivel:"))

if (c<17.5):
	x=c+0.8
	print(round(x, 1))
elif (c>=17.5 and c<35):
	y=c+1.3
	print(round(y, 1))
elif (c>=35 and c<50):
	z=c+2.1
	print(round(z, 1))
elif (c>=50):
	a=c+3
	print(round(a, 1))