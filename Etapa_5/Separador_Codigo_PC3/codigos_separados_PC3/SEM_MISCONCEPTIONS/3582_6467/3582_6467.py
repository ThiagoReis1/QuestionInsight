from numpy import *
total = 0
compra = array(eval(input()))
for x in range(size(compra)):
	if compra[x] > 160:
		compra[x] -= 25
		total += compra[x]
	else:
		total += compra[x]
print(round(total,2))