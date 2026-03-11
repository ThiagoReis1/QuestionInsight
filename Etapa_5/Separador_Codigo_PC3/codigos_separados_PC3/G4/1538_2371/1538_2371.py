x=float(input("valor de x :"))
k=int(input("valor de k:"))
l=1
d=0
s=1
t=0
m=1
while(k>t):
	m=m+s
	s=s+(((-1)**l)*x**d)
	print(x)
	t=t+1
	
	d=d+2
print(round(m,8))	
	
	