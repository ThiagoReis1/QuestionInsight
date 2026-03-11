from numpy import *
cont = 0
total_1 = 0
total_2 = 0
v = array(eval(input()))
for c in range(size(v)):
	total_1 = total_1 + v[c]
	if v[c] > 90:
		cont += 1
	else:
		total_2 = 0
	total_2 = total_1 - (6.5 * cont)
print(total_2)