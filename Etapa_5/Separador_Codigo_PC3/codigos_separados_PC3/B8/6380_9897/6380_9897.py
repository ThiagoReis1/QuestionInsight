from numpy import *

produto = input('produtos: ').upper().split(',')
cat = zeros(4, dtype=int)

for i in range(size(produto)):
	if produto[i] == 'E':
		cat[0] += 1
	elif produto[i] == 'V':
		cat[1] +=1
	elif produto[i] == 'A':
		cat[2] += 1
	elif produto[i] == 'D':
		cat[3] +=1
print(cat)