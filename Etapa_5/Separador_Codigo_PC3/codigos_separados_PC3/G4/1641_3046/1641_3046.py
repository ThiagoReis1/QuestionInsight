from numpy import *
v = array(eval(input("v: ")))
qt = 0
j = 0
for i in range(size(v)):
	if(v[i] % 3 == 0):
		qt = qt + 1
vs = zeros(qt, dtype = int)

for i in range (size(v)):
	if(v[i] % 3 == 0):
		vs[j] = i
		j = j + 1

print(qt)
print(vs)