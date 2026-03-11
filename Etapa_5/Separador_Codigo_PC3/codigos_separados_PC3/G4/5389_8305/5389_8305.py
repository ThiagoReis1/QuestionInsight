from numpy import *
r = input().upper()

v = 0
for i in r: 
	if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
		v = v + 3.15
	else:
		v = v + 4.17
print(round(v,2))

