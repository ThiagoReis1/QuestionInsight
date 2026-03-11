from math import*
x= eval(input("Digite o valor do angulo:"))
k= int(input("Digite o valor da quantidade de termos:"))
i= 1
soma= 1
a= 2
sinal = -1
while(i<k):
	soma= soma + sinal * (x**a/factorial(a))
	i= i + 1
	a = a + 2
	sinal= sinal*-1
print(round(soma,10))
