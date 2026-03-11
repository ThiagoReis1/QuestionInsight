from math import *
x=eval(input("digite o angulo:"))
k=float(input("digite a quantidade de termos:"))
i=1
cos=1

while(i<k):
	cos=cos+x**(2*i)/factorial(2*i)*(-1)**i
	i=i+1
	
print(round(cos,10))

	
	
	
