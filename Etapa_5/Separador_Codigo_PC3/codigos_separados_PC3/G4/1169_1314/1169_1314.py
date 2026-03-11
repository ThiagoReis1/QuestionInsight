n=int(input("digite o valor de n:"))
from math import*
m=0
soma=0
sinal=-1
while m<n :
	soma=soma+(sinal*sqrt(n))/(9+m)
	n=n+1
	m=m+2
	sinal=-sinal
	
print(round(soma,6))

