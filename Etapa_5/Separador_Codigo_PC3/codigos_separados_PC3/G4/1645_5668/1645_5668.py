from numpy import *
v = array(eval(input("saques: ")))
m = 0
i = 0
while i != size(v):
	if v[i] >= 2000:
		m+=1
	i+=1
j= 0
v0 = zeros(m, dtype=int)
i = 0
while i != size(v):
	if v[i] >= 2000:
		v0[j]= i
		j= j+ 1
	i = i + 1
print(m)
print(v0)