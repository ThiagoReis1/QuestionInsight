from numpy import*

m = int(input(": "))

mt = ones((m, m), dtype = int)

for i in range(mt.shape[0]):
	for j in range(mt.shape[0]):
		if i > j:
			mt[i,j] = 0
print(mt)