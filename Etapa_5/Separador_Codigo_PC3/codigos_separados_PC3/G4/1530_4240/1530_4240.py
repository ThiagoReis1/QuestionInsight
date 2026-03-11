p= int(input())
v= int(input())
cp=float(input())
cv=float(input())
o= p+v
t=0
while(o<=80000):
	o= p+p*(cp/100) + v+v*(cv/100)
	t=t+1
	print(t)
	
