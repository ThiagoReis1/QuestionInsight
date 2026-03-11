from numpy import*
a = input("Digite "). upper()
v = a.split(".")

CHN = 0
JPN = 0
KOR = 0
MGL = 0
THA = 0

vet_z = zeros(5, dtype = int)

for a in v:
	if(a == CHN):
		CHN += 1
	elif (a == JPN):
		JPN += 1
	elif (a == CHN):
		KOR += 1
	elif (a == MGL):
		MGL += 1
	elif (a == THA):
		THA += 1

vet_z[0] = CHN
vet_z[1] = JPN
vet_z[2] = KOR
vet_z[3] = MGL
vet_z[4] = THA

print(max(vet_z))
print(vet_z)