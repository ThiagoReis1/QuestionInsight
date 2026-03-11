from math import*
x = eval(input())
k = int(input())

t=1
q=0
tgh=0
a=1
sinal=1
while(x<=k):
	tgh=tgh+sinal*(x**a/factorial(a))
	t=t+1
	a=a+2
	sinal=-sinal
print(round(tgh,7))


