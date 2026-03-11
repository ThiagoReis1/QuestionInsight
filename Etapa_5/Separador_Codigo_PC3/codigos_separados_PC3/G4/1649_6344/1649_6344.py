from numpy import *

st = input("Digite a cor: ").split(',')

z = zeros(5, dtype = int)

for i in range (len(st)):
	if st[i] == "P":
		z[0] = z[0] + 1
	elif st[i] == "C":
		z[1] = z[1] + 1
	elif st[i] == "M":
		z[2] = z[2] + 1
	elif st[i] == "V":
		z[3] = z[3] + 1
	else:
		z[4] = z[4] + 1
		
print(max(z))
print(z)

