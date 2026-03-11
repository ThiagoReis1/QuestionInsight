m=int(input("massa:"))
x=m-(m*0.1)
d=1
while(x>0.5):
	x=x-(x*0.1)
	d=d+1
print(round(d,2))