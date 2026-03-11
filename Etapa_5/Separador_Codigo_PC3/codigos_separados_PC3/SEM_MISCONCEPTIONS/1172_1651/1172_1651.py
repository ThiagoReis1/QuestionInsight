from math import *
n=int(input("Qual o numero?"))
i= 1
soma=0
sinal=1
while(i<=n):
	contra= sinal* sqrt(i)/(4+(2*i+1))
	soma=soma+contra
	sinal=-sinal
	i=i+1
print(round(soma, 9))
	