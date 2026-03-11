from math import* 
x=float(input("um numero real:"))
y=int(input("um numero inteiro:"))
c=0
r=0
n=1
t=1
while(c<y):
	r=r+(x**(t)/factorial(n))
	t=t+2
	n=n+2
	c=c+1
print(round(r,9))