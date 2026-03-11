from numpy import*
v = array(eval(input()))
x = ones(size(v), dtype=int)
i = 0
v[i] = i

for i in v:
	if( v[i] != 1):
		x[:-1] = x + v[i]
		print(x)
		