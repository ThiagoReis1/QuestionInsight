x = int(input("Digite o numero de series ")) 

i = 1
soma = 0
n = 1
d = 1
sinal = 1

while(i <= x):
	soma = soma + ((sinal * n ** 3) / (5 + d)) 
	n = n + 1
	d = d + 2
	sinal = - sinal
	i = i + 1
print(round(soma,9))