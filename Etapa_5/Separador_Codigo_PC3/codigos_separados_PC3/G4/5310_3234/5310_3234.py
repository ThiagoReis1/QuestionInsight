from math import*
x=float(input("digite o valor de x "))
k=int(input("digite a quantidade de termos "))
i=0
soma=0
while(i<k):
	t=x/factorial(2*i+1)
	soma=soma+t
	i=i+1
print(round(soma,8))