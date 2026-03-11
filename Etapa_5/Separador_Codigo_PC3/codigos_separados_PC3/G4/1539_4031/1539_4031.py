x = float(input("digite um numero real: "))
soma = 1
k = 0
while (x > -1) and (x < 1) and (k >= 0):
	soma = soma + (1/1 + ((x**k)*(-1)**k))
	k = k + 1
	k = int(input("digite um numero inteiro: "))
print(round(soma, 7))