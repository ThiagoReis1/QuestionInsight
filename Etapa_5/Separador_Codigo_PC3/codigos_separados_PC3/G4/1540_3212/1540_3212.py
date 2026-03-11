from math import*
x=eval(input("angulo:"))
k=int(input("quantidade de termos:"))

a=2
b=1
c=1

while(x>=0 and k>0):
	z=(x**c)
	f=factorial(a)
	y=z/f
	y=(-1)*y
	b=b+y
	a=a+2
	c=c+1
	print(round(b,6))
