x=float(input())

if -100<=x<0:
	y=-1/x
	print(round(y,4))
elif 0<x<=100:
	y=1/x
	print(round(y,4))
else:
	print('entrada invalida')