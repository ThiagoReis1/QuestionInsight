from numpy import *
ct = input("palavra: ").upper()

i = +1
v1 = 0 
v2 = 0

for i in range(len(ct)):
	if ct [i] == "A":
		v1 = 25.12 + v1
	elif ct [i] == "E":
		v1 = 25.12 + v1
	elif ct [i] == "I":
		v1 = 25.12 + v1
	elif ct [i] == "O":
		v1 = 25.12 + v1
	elif ct [i] == "U":
		v1 = 25.12 + v1
	else: 
		v2 = 40.18 + v2
vetf = v1 + v2
print(round(vetf, 2))