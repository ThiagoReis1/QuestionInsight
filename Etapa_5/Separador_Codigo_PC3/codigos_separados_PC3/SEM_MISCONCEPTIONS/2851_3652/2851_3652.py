from numpy import *
v = array(eval(input('numeros: ')))
i = 0
total = 0
while i < size(v):
	if i >= 0:
		total = total + v[i]
		i = i + 1
	if v[i-1] == 99 :
		total = total * 2 - 99 *2
print(total)
