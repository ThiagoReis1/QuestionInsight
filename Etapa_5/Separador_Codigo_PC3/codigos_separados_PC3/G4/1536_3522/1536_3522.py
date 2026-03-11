x = float(input())
k = int(input())
sinal = 1
expoente = 1
soma = 0
t = 0
while(t < k):
	num = ((x ** expoente) / expoente) * sinal
	sinal = sinal * -1
	soma = soma + num
	t = t + 1
	expoente = expoente + 1
print(round(soma, 10))