x = float(input("digite um numero real: "))
k = int(input("digite o numero de termos: "))

soma = 0
i = 0
d = 1

while(i<k):
	soma = soma + (((-1)** i)*(x**(d))/d)
	i = i + 1
	d = d + 2
print(round(soma,6))