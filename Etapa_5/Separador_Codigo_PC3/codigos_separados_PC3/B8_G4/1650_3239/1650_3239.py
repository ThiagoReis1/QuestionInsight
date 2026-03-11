from numpy import *

a = input("Digite ").upper()
v = a.split(',')
vet_z = zeros(5, dtype=int)
P = 0
C = 0
R = 0
L = 0
B = 0

for i in range(len(v)):
	if v[i] == "P":
		P += 1
	elif v[i] == "C":
		C += 1
	elif v[i] == "R":
		R += 1
	elif v[i] == "L":
		L += 1
	elif v[i] == "B":
		B += 1

vet_z[0] = P
vet_z[1] = C
vet_z[2] = R
vet_z[3] = L
vet_z[4] = B

print(max(vet_z))
print(vet_z)