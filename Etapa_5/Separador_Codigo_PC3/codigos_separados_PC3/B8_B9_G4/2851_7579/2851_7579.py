from numpy import *

n = array(eval(input(":")))
v = 0
for x in n:
	if x != 99:
		v = v + x
		
	elif x == 99:
		v = v * 2
	
print(v)