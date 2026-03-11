from numpy import*

#passo1 = criar o vetor com 10 posições
notas = zeros(10, dtype= float)

for i in range(10):
	n = float(input())
	if 0 <= n <= 10:
		notas[i] = n

nota_minima = float(input())

c = 0

for i in range(10):
	if notas[i] >= nota_minima:
		c += 1
vet = zeros(c, dtype = float)

a = 0

for i in range(10):
	if notas[i] >= nota_minima:
		vet[a] = notas[i]
		a += 1

print(c)
print(vet)
	