from math import*
angulo = eval(input("o angulo: "))
k = int(input("quantidades de termos: "))
soma = 0
i = 0
while(i < k):
	soma = soma +  (((1)**i) * (angulo**(2*i + 1)) / (2*i + 1))
	i = i + 1
print(round(soma,7))