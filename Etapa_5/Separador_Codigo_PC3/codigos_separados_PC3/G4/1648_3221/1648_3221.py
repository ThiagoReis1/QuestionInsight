from numpy import *
f = array(eval(input()))

r = 0

for i in f:
	if i<70:
		r = r + 1
i = 0
rp = zeros(r,dtype=int)
for j in range(size(f)):
	if f[j]<70:
		rp[i]=rp[i]+j
		i = i + 1
print(r)
print(rp)