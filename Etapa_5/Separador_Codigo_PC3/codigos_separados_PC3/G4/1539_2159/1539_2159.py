
# Entradas
x = float(input("Digite um número real: "))
k = int(input("Quantidade de termos: "))

t = 0
soma = 0
f = k - 1

while (f >= t):
	soma = soma + ((-1)**t)*(x**t)
	t = t + 1
print(round(soma,7))
