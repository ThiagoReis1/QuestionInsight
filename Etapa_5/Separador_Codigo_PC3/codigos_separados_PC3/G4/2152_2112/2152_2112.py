from numpy import*
v = array(eval(input()))
i = 0
n = 0

for x in range(size(v)):
	if (v[x]%2!=1) :
		i = i + 1
		n = n + 1
	else:
		i = i + 1
		
k = size(v) - n
z = zeros(k,dtype=int)
i = 0
j = 0

for x in range(size(v)):
	if (v[x]%2!=1):
		i = i + 1
	else:
		z[j]= v[x]
		j = j + 1
		i = i + 1
print(z)