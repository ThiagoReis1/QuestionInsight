from numpy import * 

paises = str(input("")).split(',')

v = zeros(5, dtype=int)

for i in range (0, len(paises)):
	if paises[i] == "AR":
		v[0] += 1
	if paises[i] == "BR":
		v[1] += 1
	if paises[i] == "CL":
		v[2] += 1
	if paises[i] == "CO":
		v[3] += 1
	if paises[i] == "UY":
		v[4] += 1

print(max(v))
print(v)