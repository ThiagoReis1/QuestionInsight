a=float(input())
if(a<=1000):
	x=(0.05*a)
	print(round(x,2)) 
b=a-1000
if(a>1000):
	y= (0.05*1000) + b*0.1
	print(round(y,2))
	