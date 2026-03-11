from numpy import *
alu = array(eval(input()))
t= 0
for ele in alu:
	if(ele < 70):
		t = t + 1
z = zeros(t, dtype=int)
p = 0
for i in range(len(alu)):
	if(alu[i] < 70):
		z[p] = i
		p = p + 1
print(t)
print(z)