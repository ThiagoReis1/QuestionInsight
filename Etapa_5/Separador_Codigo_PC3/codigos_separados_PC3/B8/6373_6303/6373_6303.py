from numpy import *

entrada = input().split(',')
v = zeros(4, dtype=int)

for i in entrada:
	if i.upper()=='A':
		v[0]+=1
	elif i.upper()=='P':
		v[1]+=1
	elif i.upper()=='D':
		v[2]+=1
	elif i.upper()=='M':
		v[3]+=1
print(v)