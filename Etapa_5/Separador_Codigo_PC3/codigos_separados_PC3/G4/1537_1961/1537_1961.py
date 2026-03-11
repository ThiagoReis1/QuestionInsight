from math import*
x=float(input("numero:"))
k=int(input("numero:"))
soma=0
i=0
while(i<k):
	soma=soma+(x**i)/(factorial(i))
	i=i+1
print(round(soma,9))