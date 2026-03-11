from numpy import *
v = array(eval(input("face:")))
i = 0
p = 200
for n in range(0,size(v)):
	if v[i] == 1 or v[i] == 3 or v[i] == 5:
		p = p / 2
	elif v[i] == 2 or v[i] == 4 or v[i] == 6:
		p = p * 3
print(round(p, 2))