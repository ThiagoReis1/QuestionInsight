from math import*
ang=eval(input("valor do angulo: "))
k= float(input("valor de serie: "))
x=1
n=2
soma=1
while(x<k):
	soma=soma+(ang**x/factorial(2*x))*(-1)**x
	x=x+1
print(round(soma,6))
	