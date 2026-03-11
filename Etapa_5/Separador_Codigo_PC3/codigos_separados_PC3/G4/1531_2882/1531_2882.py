from math import*

x=eval(input("Angulo x: "))
k=int(input("Qtd de termos: "))
f=int(factorial(2**k))

i=0
soma=0
while(i<k):
	soma=soma+((((-1)**k)*(x**k))/f)
	i=i+1
	
	
	print(round(soma,10))