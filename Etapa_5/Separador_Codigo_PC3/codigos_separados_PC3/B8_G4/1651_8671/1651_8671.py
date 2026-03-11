from numpy import *

tp = input("Digite o tom de pele: ").upper().split(',')

v = zeros(6,dtype=int)

for i in tp:
	if i == "MC":
		v[0] += 1
	elif i == "C":
		v[1] += 1
	elif i == "CM":
		v[2] += 1
	elif i == "EM":
		v[3] += 1
	elif i == "E":
		v[4] += 1
	elif i == "ME":
		v[5] += 1

print(max(v))
print(v)
		
	