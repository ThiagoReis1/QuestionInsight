from numpy import *

turm = array(eval(input()), dtype=int)

acc = 0

for i in range(size(turm)):
	if turm[i] % 5 == 0:
		acc = acc + 1

j = 0
result = zeros(acc, dtype=int)
for i in range(size(turm)):
	if turm[i] % 5 == 0:
		result[j] = i
		j = j + 1

print(acc)
print(result)