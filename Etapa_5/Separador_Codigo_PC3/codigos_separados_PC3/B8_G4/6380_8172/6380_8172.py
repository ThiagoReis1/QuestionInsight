from numpy import *

x = input().upper().split(',')
v = zeros(4, dtype = int)

for i in x:
	if i == 'E':
		v[0] = v[0] + 1
	elif i == 'V':
		v[1] = v[1] + 1
	elif i == 'A':
		v[2] = v[2] + 1
	elif i == 'D':
		v[3] = v[3] + 1
print(v)