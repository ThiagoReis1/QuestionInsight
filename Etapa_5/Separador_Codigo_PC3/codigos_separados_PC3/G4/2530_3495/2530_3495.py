d=float(input())
tf=float(input())
j=float(input())
 
lim=d+(d*0.15)
count=0

while (d<lim):
	d=d+(j*d)
	d=d-tf
	count=count+1
	
print(count)