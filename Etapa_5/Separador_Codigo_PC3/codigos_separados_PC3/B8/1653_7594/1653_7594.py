from numpy import*

nacion = input().upper().split(',')

base0 = zeros(5, dtype = int)

for i in range(size(nacion)):
	if nacion[i] == "AR":
		base0[0] += 1
	elif nacion[i] == "BR":
		base0[1] += 1
	elif nacion[i] == "CL":
		base0[2] += 1
	elif nacion[i] == "CO":
		base0[3] += 1
	elif nacion[i] == "UY":
		base0[4] += 1

print(max(base0))
print(base0)