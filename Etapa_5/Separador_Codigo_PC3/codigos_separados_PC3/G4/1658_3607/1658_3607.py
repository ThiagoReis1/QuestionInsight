from numpy import *

entr = input()
vet = entr.split(',')

v = zeros(5, dtype=int)

for i in range(size(vet)):
	if vet[i] == "CHN":
		v[0] = v[0] + 1
	elif vet[i] == "JPN":
		v[1] = v[1] + 1
	elif vet[i] == "MGL":
		v[3] = v[3] + 1
	elif vet[i] == "KOR":
		v[2] = v[2] + 1
	else:
		v[4] = v[4] + 1

print(v[v.argmax()])
print(v)

