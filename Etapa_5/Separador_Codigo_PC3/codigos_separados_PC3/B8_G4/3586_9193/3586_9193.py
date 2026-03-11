from numpy import *

v = array(eval(input("Aneis acertados \"la ele\": ")))

i = 0
p = 0

while i < size(v):
	if v[i] == 1:
		p += 100
	elif v[i] == 2:
		p += 60
	elif v[i] == 3:
		p += 20
	i += 1
		
print(p)