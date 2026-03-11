from numpy import *
v = array([0,0,0,0,0,0])
x = input(': ').upper().split(',')
for i in range(len(x)):
	if x[i] == 'MC':
		v[0] += 1
	elif x[i] == "C":
		v[1] += 1
	elif x[i] == "CM":
		v[2] += 1
	elif x[i] == "EM":
		v[3] += 1
	elif x[i] == "E":
		v[4] += 1
	elif x[i] == "ME":
		v[5] += 1
print(max(v))
print(v)