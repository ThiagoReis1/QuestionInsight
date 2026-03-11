from numpy import*

v = array(eval(input("insira: ")))

for i in range(size(v)):
	if v[i] == 0:
		v[i] = v[i] + 9
	else:
		v[i] = v[i] - 1
		
print(v)