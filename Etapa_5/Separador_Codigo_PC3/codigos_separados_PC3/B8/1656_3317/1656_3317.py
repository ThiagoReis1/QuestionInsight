from numpy import*
ka = input("digite: ")
vetor = ka.split(',')
vr = zeros(5, dtype=int)
for cont in vetor:
	if cont.upper() == "BE":
		vr[0] = vr[0] + 1
	elif cont.upper() == "ES":
		vr[1] = vr[1] + 1
	elif cont.upper() == "FR":
		vr[2] = vr[2] + 1
	elif cont.upper() == "IT":
		vr[3] = vr[3] + 1
	elif cont.upper() == "PT":
		vr[4] = vr[4] + 1
print(max(vr))
print(vr)