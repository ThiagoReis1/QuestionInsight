from math import*
x = eval(input("x"))
k = int(input("k"))
soma = 0
i=0
while (i < k):
	soma = soma + ((x**(2*i+1))*((-1)**i))/factorial((2*i+1))
	i=i+1
print(round(soma,10))