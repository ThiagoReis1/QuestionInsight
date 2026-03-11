from math import*
x=float(input())
k=int(input())
i=0
t=1 
sinal=1
while(i<=k):
	sinal= -sinal
	conta=i + (x**i*sinal)/factorial(t)
	i=i + 2
	t= t + 2
	print(round(conta,6))