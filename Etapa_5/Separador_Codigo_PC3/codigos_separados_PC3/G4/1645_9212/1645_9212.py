from numpy import*

m = eval(input("digite numeros inteiros:"))
j = 0

vetor = zeros(len(m), dtype=int)
k = 0

for i in range(len(m)):
	if m[i] >= 2000:
		j += 1
		vetor[k] = i
		k += 1
print(j)

am = zeros(j, dtype=int)
for a in range(j):
	am[a] = vetor[a]
print(am)
		
		
