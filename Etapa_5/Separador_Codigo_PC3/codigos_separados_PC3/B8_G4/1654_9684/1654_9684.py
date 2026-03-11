from numpy import *

t = zeros(5, dtype = int)
s = input("").upper().split(',')
for x in s:
	if (x == 'AM'):
		t[0] += 1
	elif (x == 'PE'):
		t[1] += 1
	elif (x == 'MG'):
		t[2] += 1
	elif (x == 'SP'):
		t[3] += 1
	elif (x == 'RS'):
		t[4] += 1
		
print(max(t))

print(t)
		