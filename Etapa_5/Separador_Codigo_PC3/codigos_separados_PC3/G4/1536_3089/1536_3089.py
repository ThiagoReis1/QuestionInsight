from math import*
x=float(input("qual o valor de x: "))
k=float(input("qual o valor de k: "))
soma=0
t=0
i=0
sinal=1
eq=0
while(t<k):
	eq=sinal*(x**(t+1))/(1+1*i)+ eq
	t=t+1
	i=i+1
	sinal=-sinal
	soma=soma+1
print(round(eq,10))