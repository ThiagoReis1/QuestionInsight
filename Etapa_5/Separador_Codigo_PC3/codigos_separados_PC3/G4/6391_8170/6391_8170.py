from numpy import*
v = array(eval(input("Vetor de numeros: ")))

for i in range(size(v)):
	if (v[i]==0):
		v[i] = 9**3
	else:
		v[i] = (v[i]-1)**3
print(v)