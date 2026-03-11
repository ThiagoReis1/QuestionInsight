n = int(input("digite o valor de N:"))
i = 0
soma = 0
while (i < n):
	soma = soma + ((-i)**3) / (9+(i+2))
	i = i+1
print(round(soma,8))