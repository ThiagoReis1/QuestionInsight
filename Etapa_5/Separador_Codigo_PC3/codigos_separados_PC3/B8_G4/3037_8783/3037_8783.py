x=float(input())
if x<=-1 or x>=1:
	r=x**2
	print(round(r,4))
elif x>-1 and x<0 or x>0 and x<1:
	print(round(x,4))
elif x==0:
	r=1
	print(round(r,4))