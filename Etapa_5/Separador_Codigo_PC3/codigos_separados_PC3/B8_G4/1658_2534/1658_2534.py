from numpy import*
v = input(": ").upper().split(',')

cont = zeros(5, dtype=int)

for I in range (size(v)):
	if(v[I] == "CHN"):
		cont[0] = cont[0] + 1
	elif(v[I] == "JPN"):
		cont[1] = cont[1] + 1
	elif(v[I] == "KOR"):
		cont[2] = cont[2] + 1
	elif(v[I] == "MGL"):
		cont[3] = cont[3] + 1
	elif(v[I] == "THA"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)