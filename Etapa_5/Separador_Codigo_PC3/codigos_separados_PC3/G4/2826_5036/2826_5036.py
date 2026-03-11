from numpy import * 
v = array(eval(input("notas:")))
i = 0
for n in range(0, size(v)):
	if (v[i] >= 8):
		v[i] = 10
		i = i + 1
	elif v[i] <= 2:
		i = 0
		i = i + 1
	else:
		i = v[i]

w = []
x.append(w)
print(x)