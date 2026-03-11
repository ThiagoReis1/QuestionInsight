from numpy import*


v = array(eval(input("")))
v2 = array(eval(input("")))

f = 0
i = 1
k = 0

while (size(v) >= i):
	i = i + 1
	if (v[k] == "CENOURA"):
		f = f + (2 * v2[k])
	elif (v[k] == "FERRO"):
		f = f + (4 * v2[k])
	elif (v[k] == "DWARVEN"):
		f = f + (8 * v2[k])
	elif (v[k] == "ELVEN"):
		f = f + (11 * v2[k])
	else:
		f = f + (14 * v2[k])
	k = k + 1
	

print(f)

	

