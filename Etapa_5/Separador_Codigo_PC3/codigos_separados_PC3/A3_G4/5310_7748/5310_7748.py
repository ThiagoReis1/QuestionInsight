from math import*

x= float(input('x:'))
k= int(input('k'))
n=1
s=0
y=0
p=0
while(p<k):
	p=p+1
	s= x/factorial(n)
	y=y+s
	n=n+2
print (round(y,8))
	