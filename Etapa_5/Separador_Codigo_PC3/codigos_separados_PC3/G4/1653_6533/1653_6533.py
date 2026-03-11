from numpy import*

v =input("Digite as siglas do pais: ").split(',')

z = zeros (5, dtype=int)
for i in range (len(v)):
	if v[i] == "AR":
		z[0] = z[0] + 1
	elif v[i] == "BR":
		z[1] = z[1] + 1
	elif v[i] == "CL":
	   z[2] = z[2] + 1
	elif v[i] == "CO":
	   z[3] = z[3] + 1
	else:
	   z[4] = z[4] + 1

print(max(z))
print(z)
