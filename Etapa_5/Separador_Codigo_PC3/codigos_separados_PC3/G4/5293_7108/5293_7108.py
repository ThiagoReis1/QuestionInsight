n=int(input())
c=0
p=0
while n!=0:
	if((n%2)==0):
		p=p+1
		c=c+1
	
	else:
		c=c+1
	n=int(input())
	np= (p*100)/c
print(c)
print(round(np,2))
	