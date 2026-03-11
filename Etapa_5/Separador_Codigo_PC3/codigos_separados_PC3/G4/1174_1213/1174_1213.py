n = int(input("Digite um numero:"))
i = -1
y = 1
soma = 0

while(i <= n):
	z = (2*y + 1)
	soma = soma + (i**3)/(9 + z)
	y = y+1
	i = i+1
	i = i*(-1)
print(round(soma,8))	