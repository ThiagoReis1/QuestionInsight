from math import*
x= float(input('digite o valor x:'))
k= int(input('digite o numero de termos:'))

i=0
soma=0
while(i<=k):
	soma= soma + x**i/factorial(i)

	i=i+2
print(round(soma,8))
	
	