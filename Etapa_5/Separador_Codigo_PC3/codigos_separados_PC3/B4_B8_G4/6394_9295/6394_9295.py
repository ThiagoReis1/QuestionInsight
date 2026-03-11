from numpy import*
v = array(eval(input("")))

for i in range(size(v)):
	if v[i] == 0:
		v[i] += 1
	elif v[i] == 1:
		v[i] += 1
	elif v[i] == 2:
		v[i] += 1
	elif v[i] == 3:
		v[i] += 1
	elif v[i] == 4:
		v[i] += 1
	elif v[i] == 5:
		v[i] += 1
	elif v[i] == 6:
		v[i] += 1
	elif v[i] == 7:
		v[i] += 1
	elif v[i] == 8:
		v[i] += 1
	elif v[i] == 9:
		v[i] = 0
print(v)
