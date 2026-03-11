from numpy import*
mat = array(eval(input()))
v = zeros((shape(mat)[0]))
k = 0
for i in mat:
	v[k] = max(i)
	k += 1
print(max(v))