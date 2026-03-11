a=float(input())
b=int(input())
x=0
y=0
r=0
while(x<b):
	if(x%2!=0):
		y=-1
	if(x%2==0):
		y=1
	r=(a**x)*y + r
	x=x+1
print(round(r,7))