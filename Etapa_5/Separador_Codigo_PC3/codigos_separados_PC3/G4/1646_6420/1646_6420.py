from numpy import*

v = array(eval(input(":")))

acu = 0

for i in v:
	if i <= 50:
		acu += 1

saida = zeros(acu, dtype=int)
j = 0
k = 0
for b in v:
	if b <= 50:
		saida[k] = j
		k += 1
	j += 1
print(acu)
print(saida)