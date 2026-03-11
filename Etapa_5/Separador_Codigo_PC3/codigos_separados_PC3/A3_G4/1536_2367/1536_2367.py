from math import*
nr = float(input())
ni = int(input())
t=1
q=0
j =0
a=1
sinal = 1
while(t<=ni):
	j= j+sinal*(nr**a/a)
	t=t+1
	a=a+1
	sinal = -sinal
print(round(j-nr+1,10))