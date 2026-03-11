from numpy import *
v = array(eval(input("vendas: ")))
i = 0
total = 0
while i != size(v):
	total = v[i] + total
	if total >= 55:
		total = 0
	i = i+1
print(total)