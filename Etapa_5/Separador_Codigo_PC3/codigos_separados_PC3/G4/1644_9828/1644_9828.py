from numpy import *
n = array(eval(input("M: ")))
r = 0
for i in range(size(n)):
	if n[i] < 5:
		r += 1
c = zeros(r,dtype=int)
k = 0
for j in range(size(n)):
	if n[j] < 5:
		c[k] = j
		k+=1
print(r)
print(c)