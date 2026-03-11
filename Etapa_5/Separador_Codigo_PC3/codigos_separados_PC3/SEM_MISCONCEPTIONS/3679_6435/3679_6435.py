from numpy import*

N = int(input("Insira um numero: "))

matriz = zeros((N,N), dtype=int)

for i in range(N):
	for j in range(N):
		if i >= j:
			matriz[j][i] = 1
print(matriz)