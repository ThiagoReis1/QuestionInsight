from math import*
N=int(input())
sinal=1
den=7
num=1
i=0
Sc=0
while (i<N):
	Sc+=sqrt(num)/den *(sinal)
	sinal=sinal*(-1)
	num=num+1
	den=den+2
	i=i+1
print (round(Sc,10))