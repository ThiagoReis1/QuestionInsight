x = float(input(""))
k = int(input(""))

soma = 0
i = 0
sinal = 1
e = 1

while( e <= k):
	soma = soma + sinal * (x**e/e)
	sinal = - sinal
	e = e + 1
print(round(soma,6))
	