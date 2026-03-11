from numpy import *
n= float(input("digite o numero: "))
x= array(eval(input("digite o vetor x: ")))
y= array(eval(input("digite o vetor y: ")))
q= n/(n-1)
for i in range(size(x)):
	(abs(x[i])**q)= (abs(x[i])**q) + 1
	x=abs(x[i])**q**(i/size(x))
for j in range(size(y)):
	abs(y[j])**q= abs(y[j])**q + 1
	y=abs(y[j])**q**(j/size(y))
	v=x*q+y*q
print(v)

	
