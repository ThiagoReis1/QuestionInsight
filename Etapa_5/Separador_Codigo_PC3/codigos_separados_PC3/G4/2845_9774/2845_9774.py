from numpy import *

sb = array(eval(input("Substituicao: ")))
nc = zeros(size(sb), dtype=int)

for i in range(size(sb)):
	if sb[i] == 9:
		nc[i] = 0
	else:
		nc[i] = sb[i] + 1

print(nc)