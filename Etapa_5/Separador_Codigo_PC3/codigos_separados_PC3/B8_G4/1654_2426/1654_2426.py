from numpy import *
s = input("estados: ").split(',')
v = zeros(5, dtype=int)

for i in s:
	if(i == 'AM'):
		v[0] += 1
	elif(i == 'PE'):
		v[1] += 1
	elif(i == 'MG'):
		v[2] += 1
	elif(i == 'SP'):
		v[3] += 1
	elif(i == 'RS'):
		v[4] += 1
print(max(v))
print(v)