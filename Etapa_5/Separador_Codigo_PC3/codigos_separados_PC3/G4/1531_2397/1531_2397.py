from math import*
x=eval(input())
k=int(input())
soma=0
t=0
f=0
exp=0
aux=1
while(t<k):
	soma=soma + ((x**exp)/(factorial(f)))*aux
	exp=exp+2
	f=f+2
	t=t+1
	aux=aux*(-1)
print(round(soma,10))
