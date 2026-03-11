from math import*
n=int(input("digite:"))
soma=0
sinal=1
i=1
while(i<=n):
	soma=soma+sinal*sqrt(i)/(4+2*i+1)
	i= i+1
	sinal= -sinal
print(round(soma,9)) 
