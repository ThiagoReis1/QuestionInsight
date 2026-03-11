from numpy import*

v = array(eval(input("v:")))
z = zeros(size(v), dtype=int)

for i in range(size(v)):
	if v[i] == 9:
		z[i] = 0**2
	elif v[i] == 8:
		z[i] = 9**2
	elif v[i] == 7:
		z[i] = 8**2
	elif v[i] == 6:
		z[i] = 7**2
	elif v[i] == 5:
		z[i] = 6**2
	elif v[i] == 4:
		z[i] = 5**2
	elif v[i] == 3:
		z[i] = 4**2
	elif v[i] == 2:
		z[i] = 3**2
	elif v[i] == 1:
		z[i] = 2**2
	elif v[i] == 0:
		z[i] = 1**2
print(z)		
		