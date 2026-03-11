from numpy import*

frequencias = input()
frequencias = frequencias.split(",")
frequencias = array([int(freq)for freq in frequencias])

aprovados = 0

x = []

for i in range(len(frequencias)):
	if frequencias[i] >= 70:
		aprovados += 1

y = zeros(aprovados, dtype=int)
j=0
for i in range(len(frequencias)):
	if frequencias[i] >= 70:
		x.append(i)
		y[j] = i
		j += 1
print(aprovados)
print(y)