from numpy import *
vet = array(eval(input()))
a = min(vet)
b = max(vet)
c = 0.85 * a + 0.15 * b
d = 0.4 * a + 0.6 * b
saida = zeros(2, dtype=int)
i = 0
x1 = 0
x2 = 0
while (i < size(vet)):
	if ((vet[i] >= a) and (vet[i] < c)):
		x1 = x1 + 1
	if ((vet[i] >= d) and (vet[i] < b)):
		x2 = x2 + 1
	i = i +1
saida[0] = x1
saida[1] = x2
print(saida)