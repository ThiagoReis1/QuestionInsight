from numpy import*

n=input().split(",")
k=zeros(5,dtype=int)
p=0
c=0
r=0
l=0
b=0
i=0
for elemento in n:
	if(elemento=='P'):
		p=p+1
	elif(elemento=='C'):
		c=c+1
	elif(elemento=='R'):
		r=r+1
	elif(elemento=='L'):
		l=l+1
	elif(elemento=='B'):
		b=b+1	
m1=max(p,c,r)
m2=max(r,l,b)
if(m1>m2):
	print(m1)
else:
	print(m2)
k=array([p,c,r,l,b])
print(k)
	
