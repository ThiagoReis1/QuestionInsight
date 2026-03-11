N = int(input("Digite o N:"))

x = 1
c = 1
j = 1
soma = 0
k = 1
while((x <= N)):
	soma = soma + (c**3/(5 + j))  * k
	c = c + 1
	j = j + 2
	x = x + 1
	k = k * (-1)
print(round(soma,9))

	