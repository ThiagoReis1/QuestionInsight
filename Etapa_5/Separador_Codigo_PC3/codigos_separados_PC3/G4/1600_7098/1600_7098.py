from numpy import *

v = array(eval(input("valor das compras: ")))
desconto = 15/100

i = 0

while i < size(v):
	if v[i] > 80.00:
		d = v[i] * desconto
		v[i] = v[i] - d
	i = i + 1
h = sum(v)
print(round(h, 2))