from numpy import * 

v = array(eval(input('Determine: ')), dtype=int)

s = size(v)
v0 = zeros(s, dtype=int)

for i in range(s):
	if v[i] == 9:
		v0[i] = 0
	else:
		v0[i] = v[i] + 1
		
print(v0)