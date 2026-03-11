from numpy import*

q = array(eval(input("")))
h = 0 
s = 0

for i in range(size(q)):
	if(q[i] % 2 != 0):
		h = h + 1
print(h)

nv = zeros(h, dtype = int)

for j in range(size(q)):
	if(q[j] % 2 != 0):
		nv[s] = j
		s = s + 1
print(nv)
	