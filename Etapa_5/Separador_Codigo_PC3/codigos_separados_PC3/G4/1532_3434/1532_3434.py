from math import*
x = float(input("numero real: "))
k = int(input("parcela da serie: "))

soma = 0

while(k > 0):
	parcela = (x**(2*k-1)) / factorial(2*k-1)
	soma = soma + parcela
	k = k - 1
print(round(soma,9))