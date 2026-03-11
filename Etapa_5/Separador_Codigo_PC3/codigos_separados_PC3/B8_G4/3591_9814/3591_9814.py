from numpy import *

vf = array(eval(input('determine as faces do dado: ')), dtype=int)

i = 0
p = 0

while i < size(vf):
	if vf[i] % 2 == 0:
		p = p + 5
	elif vf[i] % 2 != 0:
		p = p + 10
	i += 1
	
print(p)