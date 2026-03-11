n = int(input("Digite o valor de N:"))
i = 1
soma = 0
sinal = 1
while(i <= n):
	contra = sinal * (i) ** 2 / (4 + (2 * i - 1))
	soma = soma + contra
	sinal = -sinal
	i = i + 1
print(round(soma, 8))	