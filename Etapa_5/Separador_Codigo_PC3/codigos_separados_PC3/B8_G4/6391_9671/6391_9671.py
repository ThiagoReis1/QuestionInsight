from numpy import *

num = array(eval(input("insira os numeros a serem substituidos: ")))

v = zeros(size(num), dtype=int)

for i in range(size(num)):
	if num[i] == 0:
		v[i] = 9 ** 3
	elif num[i] == 1:
		v[i] = 0 ** 3
	elif num[i] == 2:
		v[i] = 1 ** 3
	elif num[i] == 3:
		v[i] = 2 ** 3
	elif num[i] == 4:
		v[i] = 3 ** 3
	elif num[i] == 5:
		v[i] = 4 ** 3
	elif num[i] == 6:
		v[i] = 5 ** 3
	elif num[i] == 7:
		v[i] = 6 ** 3
	elif num[i] == 8:
		v[i] = 7 ** 3
	elif num[i] == 9:
		v[i] = 8 ** 3
print(v)