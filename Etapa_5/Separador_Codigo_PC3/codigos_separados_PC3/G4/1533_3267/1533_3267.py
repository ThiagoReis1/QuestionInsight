from math import*
x=float(input("digite o numero:"))
k=int(input("digite a quantidade de termos:"))
i=0
c=0
soma=0
while(c<k):
	soma=soma+(x)**c/(factorial(i))
	i=i+2
	c=c+2
print(round(soma,8))
