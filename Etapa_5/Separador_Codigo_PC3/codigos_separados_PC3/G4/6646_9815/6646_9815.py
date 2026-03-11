from numpy import *

v = array(eval(input("Insira as Notas: ")))
w = array([1, 2, 3], dtype=int)
i = 0
j = 0
x = 0

while i < size(v):
	y = v[i] * w[j]
	x += y
	i += 1
	j += 1
	
print(round(x / 6, 2))
