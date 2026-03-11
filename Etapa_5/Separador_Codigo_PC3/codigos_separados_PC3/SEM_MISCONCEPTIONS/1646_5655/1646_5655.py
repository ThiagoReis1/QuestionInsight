from numpy import *

saques = array(eval(input("Saques ")))
i = 0

for _ in range(size(saques)):
	if saques[_] <= 50:
		i = i + 1
print(i)

resultado = zeros(i, dtype = int); j = 0; y = 0

for y in range(size(saques)):
	if saques[y] <= 50:
		resultado[j] = resultado[j] + y
		j = j + 1

print(resultado)