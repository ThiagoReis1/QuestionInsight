from numpy import*
v = array(eval(input()))
l = 0
ll = 0
for i in range(0, size(v)):
	if (v[i] >= 70):
		l += 1
j = 0	
v1 = zeros(l, dtype = int)
for i in range(0, size(v)):
	if (v[i]>=70):
		v1[j] = i
		j = j+1
print(l)
print(v1)