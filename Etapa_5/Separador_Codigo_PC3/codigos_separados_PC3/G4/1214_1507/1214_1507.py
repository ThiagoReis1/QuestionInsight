from numpy import*
v = array(eval(input("pesos levantados:")))
r = 217
i = 0
k = 0
while i < size(v):
	if v[i] < r:
		k = k + 1
	i = i + 1
print(r)
print(k)