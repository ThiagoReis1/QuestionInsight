from math import *
x= int(input("qual o valor:"))
k= int(input("qual o valor: "))
soma=0
i=1
while(soma<k):
	soma=soma+(k**(2*i+1))/ factorial(2*i+1)
	i=i+1
print(round(soma,9))