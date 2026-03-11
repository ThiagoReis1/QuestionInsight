from numpy import*
t = input("").split(',')
v = zeros(5,dtype = int)
i = 0 
for i in range(size(t)):
	if t[i] == "P":
		v[0] = v[0] + 1
	elif t[i] == "C":
		v[1] = v[1] + 1
	elif t[i] == "M":
		v[2] = v[2] + 1
	elif t[i] == "V":
		v[3] = v[3] + 1
	elif t[i] == "A":
		v[4] = v[4] + 1
	i = i + 1
print(max(v))
print(v)