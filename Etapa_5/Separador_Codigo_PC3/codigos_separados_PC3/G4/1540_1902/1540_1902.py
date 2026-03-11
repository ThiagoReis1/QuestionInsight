from math import*
x=eval(input(":"))
k=int(input(":"))
soma=0
t=0#contadora
a=0
indice=1
while(t<k):
	
	soma=soma+(indice)*(x**(t))/factorial(a)
	indice=-indice
	t=t+1#contadora
	a=a+2
print(round(soma,6))	
