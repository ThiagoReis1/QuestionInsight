from numpy import*

v = array(eval(input("Digite: ")))

for i in range(size(v)):
	if v[i] == 9:
		v[i] = 0
	else:
		v[i] = (v[i]+1)**2
print(v)