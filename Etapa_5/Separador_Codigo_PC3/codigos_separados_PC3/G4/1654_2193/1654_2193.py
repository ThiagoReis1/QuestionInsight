from numpy import *

vet = input("").split(',')
n = zeros(5, dtype=int)

for i in vet:
	if (i == "AM"):
		n[0] = n[0] + 1
	if (i == "PE"):
		n[1] = n[1] + 1
	if (i == "MG"):
		n[2] = n[2] + 1
	if (i == "SP"):
		n[3] = n[3] + 1
	if (i == "RS"):
		n[4] = n[4] + 1
print(max(n))
print(n)