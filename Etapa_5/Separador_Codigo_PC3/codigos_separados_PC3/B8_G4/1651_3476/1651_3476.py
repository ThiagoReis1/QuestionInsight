from numpy import*
v = input("Digite: ")
vet2 = v.split(',')
vetr = zeros(6,dtype=int)
for cont in vet2:
	if cont.upper() == "MC":
		vetr[0] = vetr[0] + 1 
	elif cont.upper() == "C":
		vetr[1] = vetr[1] + 1
	elif cont.upper() == "CM":
		vetr[2] = vetr[2] + 1
	elif cont.upper() == "EM":
		vetr[3] = vetr[3] + 1
	elif cont.upper() == "E":
		vetr[4] = vetr[4] + 1
	elif cont.upper() == "ME":
		vetr[5] = vetr[5] + 1
print(max(vetr))
print(vetr)