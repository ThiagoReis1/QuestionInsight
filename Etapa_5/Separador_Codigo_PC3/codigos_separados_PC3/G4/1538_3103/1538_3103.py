x = float(input("Qual o numero real escolhido?: "))
k = int(input("Qual a quantidade de termos da serie?: "))
t = 0
i = 0
soma = 0
while(t < k):
	soma = soma + (-1) ** t * x ** i
	i = i + 2
	t = t + 1
print(round(soma,8))	