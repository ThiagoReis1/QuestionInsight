c=int(input())

if c<17.5:
	x=c+1.5
	print(round(x,2))
elif 15.5<=c<35.0:
	x=c+2.3
	print(round(x,2))
elif 35<=c<50:
	x=c+3.3
	print(round(x,2))
else:
	x=c+4.7
	print(round(x,2))