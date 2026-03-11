from math import*

x= float(input("x: "))
k=int(input("k:"))
c=1
pot=1
a=0
sinal=1
ct=0

while ct<k:
	cos= sinal*(x**pot)/(factorial(c))
	a=cos+a
	pot=pot+2
	c=c+2
	sinal=-1*sinal
	ct=ct+1
print(round(a,8))