from math import*
x=eval(input("angulo x: "))
k= int(input("K: "))
ct=0
c=0
sinal=1
pot=0
a=0
while ct<k:
	cos=sinal*(x**pot)/(factorial(c))
	a=cos+a
	c=c+2
	ct=ct+1
	pot=pot+1
	sinal=-1*sinal

print(round(a,6))

	