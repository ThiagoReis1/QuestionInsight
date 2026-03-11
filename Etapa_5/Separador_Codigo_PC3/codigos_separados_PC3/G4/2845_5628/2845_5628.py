from numpy import *

v1 = array(eval(input('Digite os valores: ')))

for i in range(size(v1)):
	if v1[i] == 9:
		v1[i] = 0
	else:
		v1[i] = v1[i] + 1
print(v1)