x=float(input())
k=int(input())
c=1
a= x

while(c<k and x>=-1 and x<=1):
	den= c*2 + 1
	a= a - (-1)**(c+1) * (x**(2*c+1))/den
	c= c + 1
	
print(round(a,6))