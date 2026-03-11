from numpy import *

dado = array(eval(input()))
total = 0
i = 0

while i < size(dado):
	if dado[i] == 1:
		total += 10
	elif dado[i] == 2:
		total += 5
	elif dado[i] == 4:
		total += 5
	elif dado[i] == 5:
		total += 20
	elif dado[i] == 6:
		total += 10
	i += 1
print(total)