from numpy import *

s = input("").upper().split(',')
v = zeros(6, dtype = int)
a = 0

for i in range(size(s)) :
	if (s[i] == "MC") :
		v[0] = v[0] + 1
	elif (s[i] == 'C') :
		v[1] = v[1] + 1
	elif (s[i] == 'CM') :
		v[2] = v[2] + 1
	elif (s[i] == 'EM') :
		v[3] = v[3] + 1
	elif (s[i] == 'E') :
		v[4] = v[4] + 1
	elif (s[i] == 'ME') :
		v[5] = v[5] + 1

print(max(v))
print(v)