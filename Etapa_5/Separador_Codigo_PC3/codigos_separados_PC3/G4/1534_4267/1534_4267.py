x = float(input("Digite um numero real: "))
k = int(input("Digite um numero inteiro: "))

i = 0
soma = 0
while(i<k):
	soma = soma + ((x**(2*i + 1))/(2*i + 1))
	i = i + 1
print(round(soma,7))