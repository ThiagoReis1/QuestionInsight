from numpy import*

num = array(eval(input()))
v = zeros(size(num), dtype=int)

for i in range(0, size(num)):
	x = num[i] -1
	if x == -1:
		v[i] = 9**3
	else:
		v[i] = x**3
	
print(v)