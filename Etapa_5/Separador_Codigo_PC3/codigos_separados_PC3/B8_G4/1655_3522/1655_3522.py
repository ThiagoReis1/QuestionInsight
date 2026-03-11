from numpy import*
x = input("")
vet = x.split(',')
v = 1
for cont in vet:
	if cont.upper() == "AC":
		V[0] = V[0]
	elif cont.upper() == "AM":
		v[1] = v[1]
	elif cont.upper() == "PA":
		v[2] = v[2]
	elif cont.upper() == "RO":
		v[3] = v[3]
	elif cont.upper() == "RR":
		V[4] = V[4]
		v = v + 1
print(max(v))
print(v)