x = float(input("Digite um numero: "))
k = int(input("Digite a quantidade de termos: "))

soma = 0
i = 2
e = 0

while e < k:
	soma = soma + (x/i)
	i = i + 2
	e = e + 1
	
print(round(soma,8))