y= float(input())

if (y<=-1) or (y>=1):
	print(round(y,2))
elif (-1<y<0) or (0<y<1):
	print(round(1,2))
else :
	print(round(2,2))
