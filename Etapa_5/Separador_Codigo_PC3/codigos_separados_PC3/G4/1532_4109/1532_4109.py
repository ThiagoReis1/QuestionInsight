from math import*
x=float(input('Digite um numero: '))
k=int(input('Quantidade de termos: '))
soma=0
i=1
t=0
while(t<k):
	soma = soma + ((x)**i) / (factorial(i))
	i = i + 2
	t = t + 1
print(round(soma, 9))