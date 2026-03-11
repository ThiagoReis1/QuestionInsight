from numpy import*
v = array(eval(input()))
x = 0
for i in range(size(v)):
	if(v[i]%2!=0):
		x = x + 1
z = zeros(x, dtype=int)
j = 0
for i in range(size(v)):
	if(v[i]%2!=0):
		z[j] = v[i]
		j = j + 1
print(z)