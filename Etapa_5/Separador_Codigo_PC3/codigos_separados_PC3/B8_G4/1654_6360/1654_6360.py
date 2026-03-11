from numpy import *
s = input().split(',')
v = zeros(5, dtype = int)

for i in range(size(s)):
	if s[i] == 'AM':
		v[0] = v[0] + 1
	elif s[i] == 'PE':
		v[1] = v[1] + 1
	elif s[i] == 'MG':
		v[2] = v[2] + 1
	elif s[i] == 'SP':
		v[3] = v[3] + 1
	elif s[i] == 'RS':
		v[4] = v[4] + 1
print(max(v))
print(v)