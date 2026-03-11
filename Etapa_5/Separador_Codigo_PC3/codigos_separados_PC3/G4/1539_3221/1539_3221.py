x = float(input())
k = int(input())

e = 0
soma = 0
cont = 0
sinal = 0

while cont < k :
	t = x**e
	sinalizador = (-1)**(sinal + 2)
	soma = soma + t*sinalizador
	e = e + 1
	cont = cont + 1
	sinal = sinal + 1
print(round(soma,7))