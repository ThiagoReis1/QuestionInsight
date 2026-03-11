from numpy import *
notas = input("INSERIR: ").upper().split(',')
v = zeros(5, dtype = int)

for i in notas:
	if i == "A":
		v[0] += 1
	elif i == "B":
		v[1] += 1
	elif i == "C":
		v[2] += 1
	elif i == "D":
		v[3] += 1
	elif i == "E":
		v[4] += 1
print(v)