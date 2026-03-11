from numpy import *

v = array(eval(input("Coloque o valor dos produtos comprados: ")))

a = ones(size(v), dtype=float)

i = 0

while (i < size(a)):
	if (v[i] <= 80):
		a[i] = v[i]
	else:
		a[i] = 0.85 * v[i]
	i = i + 1
	
print(round(sum(a), 2))