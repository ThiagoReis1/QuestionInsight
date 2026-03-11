from math import *
x=eval(input("valor: "))
y=int(input("valor: "))
i=0
k=0
while(i<y):
	sgn=(-1)**i
	k=k+(sgn*((x**(2*i))/factorial(2*i)))
	i=i+1
print(round(k,10))
