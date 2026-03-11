from numpy import*

v = input("Digite qual deseja: ").upper().split(',')
cont = 0
vz = zeros(4, dtype = int)

for i in range(size(v)):
	if v[i] == "A":
		vz[0] = vz[0] + 1
	elif v[i] == "B":
		vz[1] = vz[1] + 1
	elif v[i] == "L":
		vz[2] = vz[2] + 1
	elif v[i] == "H":
		vz[3] = vz[3] + 1

print(vz)