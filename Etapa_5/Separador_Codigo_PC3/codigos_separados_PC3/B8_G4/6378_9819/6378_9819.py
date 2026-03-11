from numpy import *

cont = input("insira a contagem de notas:  ").upper().split(",")
cat = zeros(4, dtype=int)
for v in cont:
	if v == "C":
		cat[0] += 1
	elif v == "D":
		cat[1] += 1
	elif v == "V":
		cat[2] += 1
	elif v == "U":
		cat[3] += 1
print(cat)